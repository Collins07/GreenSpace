from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_posts')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='business_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='business_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_likes')

    def __str__(self):
        return f'{self.user.username} likes {self.post}'


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_followers')

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'

