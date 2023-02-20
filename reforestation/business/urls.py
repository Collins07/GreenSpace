from django.conf import settings
from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    # path('post/edit/<int:pk>/', views.post_edit, name='post_update'),
    # path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('user/<str:username>/', ProfileView.as_view(), name='profile'),
    path('user/edit/', views.profile_edit, name='edit_profile'),
    path('post_like_ajax/', views.post_like_ajax, name='post_like_ajax'),
    path('post/<int:pk>/comment/', views.comment_create, name='post_comment'),
    path('user/<str:username>/follow/', views.follow_user, name='follow_user'),
    path('user/<str:username>/unfollow/', views.unfollow_user, name='unfollow_user'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)