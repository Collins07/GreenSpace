# from django.shortcuts import render

# # Create your views here.
# def business(request):
#     return render (request, 'business/index.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Profile, Post, Comment, Like
from .forms import PostForm, CommentForm, ProfileForm


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'business/post_create.html', {'form': form})


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'business/post_list.html', {'page_obj': page_obj})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    comment_form = CommentForm()
    user_likes_post = Like.objects.filter(post=post, user=request.user).exists()
    return render(request, 'business/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_likes_post': user_likes_post
    })


@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if created:
        messages.success(request, 'You liked the post!')
    else:
        messages.warning(request, 'You already liked the post!')
    return redirect('post_detail', pk=pk)


@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(post=post, user=request.user).first()
    if like:
        like.delete()
        messages.success(request, 'You unliked the post!')
    else:
        messages.warning(request, 'You have not liked the post yet!')
    return redirect('post_detail', pk=pk)


@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        messages.success(request, 'Your comment has been created!')
    return redirect('post_detail', pk=pk)


@login_required
def follow_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.profile.following.filter(pk=user.profile.pk).exists():
        messages.warning(request, f'You are already following {user.username}!')
    else:
        request.user.profile.following.add(user.profile)
        messages.success(request, f'You are now following {user.username}!')
    return redirect('profile_detail', username=username)


@login_required
def unfollow_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user.profile.following.filter(pk=user.profile.pk).exists():
        request.user.profile.following.remove(user.profile)
        messages.success(request, f'You have unfollowed {user.username}.')
    else:
        messages.warning(request, f'You are not following {user.username}!')
    return redirect('profile_detail', username=username)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile_detail', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'business/profile_edit.html', {'form': form})


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-created_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    user_likes = Like.objects.filter(user=user)
    return render(request, 'business/profile_detail.html', {
        'user': user,
        'page_obj': page_obj,
        'user_likes': user_likes,
    })


@login_required
def post_like_ajax(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, pk=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if created:
        response = {'result': 'liked'}
    else:
        like.delete()
        response = {'result': 'unliked'}
    return JsonResponse(response)
