from django.urls import path
from .views import RegisterPage,LoginPage,LogoutPage, BlogPage, SinglePostPage,UpdateCommentPage,DeleteCommentPage, AboutMyPage, ContactPage

app_name = 'blog'

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('', BlogPage.as_view(), name='blog'),
    path('post/<int:pk>', SinglePostPage.as_view(), name='post'),
    path('about/', AboutMyPage.as_view(), name='about'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('update_comment/<int:post_id>/<int:pk>', UpdateCommentPage.as_view(), name='update_comment'),
    path('delete_comment/<int:post_id>/<int:pk>', DeleteCommentPage.as_view(), name='delete_comment'),
    
]