from django.contrib import admin
from django.urls import path
from myapp import views
# from .views import execute_project

urlpatterns = [
    path('',views.index ,name='index'),
    path('Project',views.Project ,name='Project'),
    path('about',views.about ,name='about'),
    path('resume',views.resume ,name='resume'),
    path('contact',views.contact ,name='contact'),
    path('calculator/',views.calculator ,name='calculator'),
    path('Converter/',views.Converter ,name='Converter'),
    path('temp_Convert/',views.temp_Convert ,name='temp_Convert'),
    path('Least_Square_Method',views.matrix_view, name='run_code'),
    path('Company',views.Company, name='Company'),
    path('Guess_Game',views.guess_game, name='guess_game'),
]
