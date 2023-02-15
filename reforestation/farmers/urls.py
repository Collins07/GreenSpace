from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('' ,views.farmer, name='farmer'),
     path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('new/status/<username>', views.new_status, name='newStatus'),
    path('post/<id>', views.post_comment, name='comment'),
    path('search/', views.search_profile, name='search'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('like', views.like_post, name='like_post'),
    path('single_image/likes/<id>', views.single_image_like, name='singleImageLike'),

]