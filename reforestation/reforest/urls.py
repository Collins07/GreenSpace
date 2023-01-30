from django.urls import path
from . import views
 
urlpatterns = [
    path('' ,views.index, name='index'),
    path('add_trees' ,views.add_trees, name='add_trees'),
    path('home' ,views.home, name='home'),

]