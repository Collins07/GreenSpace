from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Reforest

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    return render(request, 'reforest/index.html')



def add_trees(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'reforest/add_trees.html', context)



def home(request):
    return render(request, 'reforest/home.html')

