#from django.conf.urls import url
#from . import views
#from django.urls import re_path as url
#from django.urls import re_path 
#from django.urls import include, path   
#from . import views
#from django import urls as url#, views
from django.urls import re_path as url
#from django.urls import path as url    
from catalog import views 

urlpatterns = [
    url(r'^$', views.index, name='index')
    #r'^$' expresion reg cuando la peticion sea nada dispara la funcion index del modulo views
]

