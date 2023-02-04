from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Reforest
from django.contrib import messages

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    reforest = Reforest.objects.all()
    context = {
        'reforest': reforest,

    }
    return render(request, 'reforest/index.html', context)



def add_trees(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST,
    }
    
    if request.method == 'POST':
        trees_planted = request.POST['trees_planted']

        if not trees_planted:
            messages.error(request,'Number of trees planted required !!!')
            return render(request, 'reforest/add_trees.html', context)
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']
        
    if request.method == 'POST':
        description = request.POST['description']

        if not description:
            messages.error(request,' The name of your group is required !!!')
            return render(request, 'reforest/add_trees.html', context)
        
        Reforest.objects.create(owner=request.user, trees_planted=trees_planted, description=description, date=date, category=category)
        messages.success(request, 'Data saved successfully')

        return redirect('index')

    return render(request, 'reforest/add_trees.html', context)    



def home(request):
    return render(request, 'reforest/home.html')

