from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Recipie
from .forms import RecipieForm
from django.contrib.auth import authenticate, login, logout#, signup
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required( login_url='/login')
def home(request):
	recipies = Recipie.objects.all()
	return render(request, 'recpie/home_page.html', {'recipies': recipies})

@login_required( login_url='/login')
def create_recipie(request):
	if request.method == 'GET':
		return render(request, 'recpie/create_page.html',{})
	print request.POST
	form = RecipieForm(request.POST)
	if form.is_valid():
		form.save()
	else:
		return render(request, 'recpie/create_page.html',{'errors': form.errors})
	# recipie_name = request.POST['recipie_name']
	# ingrediants = request.POST['ingrediants']
	# process = request.POST['process']
	# Recipie.objects.create(recipie_name=recipie_name,ingrediants=ingrediants, process=process)
	# recipies = Recipie.objects.all()
	# return render(request, 'recpie/home_page.html', {'recipies': recipies})
	return HttpResponseRedirect('/')
 
@login_required( login_url='/login')
def detail_page(request, recipie_id):
	recipie = Recipie.objects.get(id=recipie_id)
	return render(request, 'recpie/detail_page.html', {'recipie': recipie})

def loginview(request):
	if request.method == 'GET':
		return render(request, 'recpie/login_html.html', {})
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect('/')
			# recipies = Recipie.objects.all()
			# return render(request, 'recpie/home_page.html', {'recipies': recipies})
		else:
			return render(request, 'recpie/login_html.html', {'error': 'Invalid Username or Password'})

def logoutview(request):
	logout(request)
	return HttpResponseRedirect('/login')
# def signupview(request):
# 	if request.method =='GET':
# 		return render(request,'recipie/signup_html.html',{})
# 	else:
#     	first_name=request.POST['first_name']
#     	last_name=request.POST['last_name']
#     	return render(request, 'recpie/signup_html.html', {'error': 'Invalid Username or Password'})
	