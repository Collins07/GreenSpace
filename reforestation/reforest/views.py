from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'reforest/index.html')

def add_trees(request):
    return render(request, 'reforest/add_trees.html')

def home(request):
    return render(request, 'reforest/home.html')

