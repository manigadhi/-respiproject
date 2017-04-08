from django.conf.urls import include, url
from django.contrib import admin
from respies.views import home, create_recipie, detail_page, loginview, logoutview#,signupview

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_page/$', create_recipie, name='create_recipie'),
    url(r'^login/$', loginview, name='login'),
    url(r'^logout/$', logoutview, name='lohout'),
    # url(r'^signup/$', signupoview, name='signup'),
    url(r'^detail_page/(?P<recipie_id>[0-9]+)/$', detail_page, name='detail_page'),
]
