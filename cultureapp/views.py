from django.shortcuts import render
from django.http  import HttpResponse
from cultureapp.models import Booking, Profile, visitplan, services

# Create your views here.
def index(request):
    plans = visitplan.objects.all().order_by('price')
    service = services.objects.all()

    return render(request, 'index.html', {'plans': plans, 'service': service})
def about(request):
    return render(request, 'about.html')