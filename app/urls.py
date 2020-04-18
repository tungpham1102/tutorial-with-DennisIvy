from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #API data
    path('tests_api/', views.tests_data_api),
    #Create test
    path('create_test/', views.create_test),
    #Create test
    path('update_test/', views.update_test),
    path('delete_test/', views.delete_test)
]