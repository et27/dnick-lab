from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from .models import MobilePhone
from datetime import datetime

# Create your views here.

def index(request):
    # Show flights in the past
    mobiles = MobilePhone.objects.filter(year_of_production__lte=datetime.now().date())
    context = {'mobile_list': mobiles, 'Lab4-DNICK': 'MobileApp'}
    return render(request, 'index.html', context)

def details(request, mobile_id):
    mobiles = MobilePhone.objects.filter(id=mobile_id).first()
    context = {'mobile_data': mobiles, 'Lab4-DNICK': 'MobileApp'}
    return render(request, 'details.html', context)