from django.contrib import admin
from django.urls import path
from core.views import create_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_customer, name='create-customer')
]
