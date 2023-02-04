from django.urls import path
from . import views
  
urlpatterns = [
    path('' ,views.index, name='index'),
    path('add_trees' ,views.add_trees, name='add_trees'),
    path('edit_trees/<int:id>' ,views.reforest_edit, name='reforest-edit'),
    path('home' ,views.home, name='home'),

]