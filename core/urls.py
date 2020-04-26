from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('create-order/<int:pk>', views.create_order, name='create-order'),
    path('update-order/<int:pk>', views.update_order, name='update-order'),
    path('delete-order/<int:pk>', views.delete_order, name='delete-order'),
]