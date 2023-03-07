from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from .models import Category, Reforest
from django.contrib import messages
from django.core.paginator import Paginator
import json
import datetime

# Create your views here.
def search_reforest(request):
    if request.method == 'POST':
      search_str=json.loads(request.body).get('searchText')
      reforests = Reforest.objects.filter(
          trees_planted__istartswith=search_str) | Reforest.objects.filter(
          date__istartswith=search_str) | Reforest.objects.filter(
          description__icontains=search_str) | Reforest.objects.filter(
          category__icontains=search_str,owner=request.user)
      data = reforests.values()
      return JsonResponse(list(data), safe=False)


@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    reforest = Reforest.objects.all()

    paginator=Paginator(reforest, 4)
    page_number = request.GET.get('page')
    page_obj= Paginator.get_page(paginator,page_number)
    context = {
        'reforest': reforest,
        'page_obj': page_obj,

    }
    return render(request, 'reforest/index.html', context)

@login_required(login_url='/authentication/login')
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



@login_required(login_url='/authentication/login')
def reforest_edit(request, id):
    reforest = Reforest.objects.get(pk=id)
    categories = Category.objects.all()

    context = {
        'reforest': reforest,
        'values': reforest,
        'categories': categories
    }
    if request.method == 'GET':
        
        return render(request, 'reforest/edit_trees.html', context)
    if request.method == 'POST':
        trees_planted = request.POST['trees_planted']

        if not trees_planted:
            messages.error(request,'Number of trees planted required !!!')
            return render(request, 'reforest/edit_trees.html', context)
        description = request.POST['description']
        date = request.POST['date']
        category = request.POST['category']
        
    if request.method == 'POST':
        description = request.POST['description']

        if not description:
            messages.error(request,' The name of your group is required !!!')
            return render(request, 'reforest/edit_trees.html', context)
        

        reforest.owner=request.user
        reforest.trees_planted=trees_planted
        reforest.description=description
        reforest.date=date
        reforest.category=category

        reforest.save()
        messages.success(request, 'Your data has been updated successfully')

        return redirect('index')


@login_required(login_url='/authentication/login')
def reforest_delete(request,id):
    reforest = Reforest.objects.get(pk=id)
    reforest.delete()
    messages.error(request, 'Your data has been deleted')
    return redirect('index')

def reforest_category_summary(request):
    todays_date = datetime.date.today()
    six_months_ago= todays_date - datetime.timedelta(days=180)
    reforests = Reforest.objects.filter(date__gte=six_months_ago, date_lte=todays_date)
    finalrep  = {}

    def get_category(reforest):
        return reforest.category
    
    category_list= list(set(map(get_category, reforests)))

    def get_reforest_category_trees_planted(category):
        trees_planted=0
        filtered_by_category = reforests.filter(category=category)

        for item in filtered_by_category:
            trees_planted += item.trees_planted

        return trees_planted

    for x in reforests:
        for y in category_list:
            finalrep[y] = get_reforest_category_trees_planted(y)



    return JsonResponse({"reforest_category_data": finalrep}, safe=False)        