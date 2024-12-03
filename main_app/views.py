from django.shortcuts import render
from .models import Fish

# Create your views here.
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def fish_index(request):
    fishs = Fish.objects.all() 
    return render(request, 'fishs/index.html', {'fishs': fishs})

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fishs/detail.html', {'fish': fish})