from django.shortcuts import render
from .models import AppVariety
from django.shortcuts import get_object_or_404
# Create your views here.

def all_apps(request):
    apps = AppVariety.objects.all()
    return render(request,'firstApp/all_apps.html', {'apps':apps})

def app_detail(request, app_id):
    app = get_object_or_404(AppVariety, pk = app_id)
    return render(request,'firstApp/app_detail.html', {'app':app})



