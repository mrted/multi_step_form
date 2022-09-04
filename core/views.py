from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Customer


def create_customer(request):
    if request.method == 'POST' and 'profile_pic' in request.FILES:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        profile_pic = request.FILES['profile_pic']
        try:
            customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                profile_pic=profile_pic, 
                )
            customer.save()
            messages.success(request, 'Customer created successfully')
        except:
            messages.error(request, 'Customer creation failed')
    return render(request, 'create-customer.html')

