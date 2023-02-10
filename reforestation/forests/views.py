
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from .models import Forest, Reason
from django.contrib import messages
from django.core.paginator import Paginator
# from .userpreferences.models import UserPrefrence
import json


# Create your views here.


@login_required(login_url='/authentication/login')
def forest(request):
    categories = Reason.objects.all()
    forest = Forest.objects.all()

    paginator=Paginator(forest, 4)
    page_number = request.GET.get('page')
    page_obj= Paginator.get_page(paginator,page_number)
    context = {
        'forest': forest,
        'page_obj': page_obj,

    }
    return render(request, 'forests/index.html', context)

@login_required(login_url='/authentication/login')
def add_forest(request):
    reasons = Reason.objects.all()
    context = {
        'reasons': reasons,
        'values': request.POST,
    }

    # if request.method == 'GET':
    #     trees_planted = request.POST['trees_planted']
    
    if request.method == 'POST':
        trees_planted = request.POST['trees_planted']

        if not trees_planted:
            messages.error(request,'Number of trees replaced required !!!')
            return render(request, 'forests/add_forest.html', context)
        description = request.POST['description']
        date = request.POST['date']
        reason = request.POST['reason']
        
    if request.method == 'POST':
        description = request.POST['description']

        if not description:
            messages.error(request,' The name of your group is required !!!')
            return render(request, 'forests/add_forest.html', context)
        
        Forest.objects.create(owner=request.user, trees_planted=trees_planted, description=description, date=date, reason=reason)
        messages.success(request, 'Data saved successfully')

        return redirect('forest')

    return render(request, 'forests/add_forest.html', context)