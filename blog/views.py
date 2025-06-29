from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment, Category, CustomUser
from .forms import UserForm, LoginForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

# Create your views here.



class RegisterPage(TemplateView):
    model  = CustomUser
    template_name = 'blog/register.html'
    form_class = UserForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        last_post = Post.objects.last()
        return render(request, self.template_name, {'form': form, 'last_post': last_post})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        last_post = Post.objects.last()
        if form.is_valid():
            form.save()
            return redirect('blog:blog')
        return render(request, self.template_name, {'form': form, 'last_post': last_post})

class LoginPage(TemplateView):
    template_name = 'blog/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        last_post = Post.objects.last()
        return render(request, self.template_name, {'form': form, 'last_post': last_post})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        last_post = Post.objects.last()

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('blog:blog')  
            else:
                form.add_error(None, 'Username yoki parol noto‘g‘ri!')

        return render(request, self.template_name, {'form': form, 'last_post': last_post})

class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('blog:blog')
    
class BlogPage(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by('-created_at')
        context['last_post'] = Post.objects.last()
        context['posts'] = posts
        return context

class SinglePostPage(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        categories = Category.objects.all()
        posts = Post.objects.all()
        last_post = Post.objects.last()
        context = {
            'post': post,
            'form': form,
            'comments': comments,
            'categories': categories,
            'posts': posts,
            'last_post': last_post,
        }
        return render(request, 'blog/post.html', context)

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('blog:login')
        post = Post.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect('blog:post', pk=pk) 

        comments = Comment.objects.filter(post=post).order_by('-created_at')
        categories = Category.objects.all()
        posts = Post.objects.all()
        last_post = Post.objects.last()
        context = {
            'post': post,
            'form': form,
            'comments': comments,
            'categories': categories,
            'posts': posts,
            'last_post': last_post,
        }
        return render(request, 'blog/post.html', context)

class UpdateCommentPage(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['last_post'] = Post.objects.last()
        return context
    
    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('blog:post', args=[post_id])
    
class DeleteCommentPage(DeleteView):
    model = Comment
    template_name = 'blog/post.html'
    
    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('blog:post', args=[post_id])
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['last_post'] = Post.objects.last()
        return context


class AboutMyPage(TemplateView):
    template_name = 'blog/about.html'
    def get(self, request, *args, **kwargs):
        last_post = Post.objects.last()
        return render(request, self.template_name, {'last_post': last_post})
class ContactPage(TemplateView):
    template_name = 'blog/contact.html'
    def get(self, request, *args, **kwargs):
        last_post = Post.objects.last()
        return render(request, self.template_name, {'last_post': last_post})  
     





