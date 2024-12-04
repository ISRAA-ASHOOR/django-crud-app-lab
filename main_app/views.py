from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse

# Define the home view function

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fish-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def fish_index(request):
    fishs = Fish.objects.filter(user=request.user)
    return render(request, 'fishs/index.html', {'fishs': fishs})

@login_required
def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    feeding_form = FeedingForm()
    return render(request, 'fishs/detail.html', {
        'fish': fish, 'feeding_form': feeding_form
    })

class FishCreate(LoginRequiredMixin, CreateView):
    model = Fish
    fields = ['name', 'breed', 'description']
    success_url = '/fishs/'
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
    model = Fish
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description']

class FishDelete(LoginRequiredMixin, DeleteView):
    model = Fish
    success_url = '/fishs/'

@login_required
def add_feeding(request, fish_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.fish_id = fish_id
        new_feeding.save()
    return redirect('fish-detail', fish_id=fish_id)