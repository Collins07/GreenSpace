from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('' ,views.index, name='index'),
    path('add_trees' ,views.add_trees, name='add_trees'),
    path('edit_trees/<int:id>' ,views.reforest_edit, name='reforest-edit'),
    path('delete_trees/<int:id>' ,views.reforest_delete, name='reforest-delete'),
     path('search-reforest' , csrf_exempt(views.search_reforest), name='search_reforest'),
    path('home' ,views.home, name='home'),

]