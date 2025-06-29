from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class CustomUser(AbstractUser):
    image = models.FileField(upload_to="user-photo/", default="user-photo/user-default.jpg")

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True
    )

    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
class Post(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    video = models.FileField(upload_to="post-video/", null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="post-image", null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Comment(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL ,related_name="comments", null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name="comments")
    comment = models.TextField()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.user} - {self.post}"









