from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'reforest/index.html')

def add_trees(request):
    return render(request, 'reforest/add_trees.html')

