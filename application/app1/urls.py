
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('products', views.products),
    path('customers', views.customers),


]
