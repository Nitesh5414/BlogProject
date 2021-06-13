from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from blogapp.models import Post                  # import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (               # import generic views
        TemplateView,
        ListView,
        DetailView,
        CreateView,
        UpdateView, 
        DeleteView
        )
# Create your views here.

############### views for index page ##################
class IndexPageView(TemplateView):
    template_name = 'blogapp/index.html'

###################### views for read post ################
class PostListView(LoginRequiredMixin, ListView):
    model               = Post
    template_name       = 'blogapp/home.html'
    context_object_name  = 'posts'
    # login_url            = '/login/'                        #this url give in settings.py
    ordering        = ['-date_posted']  
    paginate_by = 3


###################### views for user post ################
class UserPostListView(LoginRequiredMixin, ListView):
    model               = Post
    template_name       = 'blogapp/user_post.html'
    context_object_name  = 'posts'
    # login_url            = '/login/'                        
    # ordering        = ['-date_posted']     

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
          

##################### DetailView for post ######################
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


##################### view for create post #####################
class PostCreateView(LoginRequiredMixin, CreateView):
    model        = Post
    template_name = 'blogapp/new_post.html'
    fields         = ['title', 'content']


    ### method for author_id set ###############
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


################## view for update post    ######################
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model            = Post
    template_name    = 'blogapp/update_post.html'
    fields           = ['title', 'content']

    ### method for user set ###############
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


######################### view for delete post ###############
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blogapp/delete_post.html'
    success_url = reverse_lazy('blog-post')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False