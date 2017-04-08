from django.forms import ModelForm
from .models import Recipie


class RecipieForm(ModelForm):
	class Meta:
		model = Recipie
		fields = ['recipie_name', 'ingrediants', 'process']