from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import BlogForm, CommentForm
from django.urls import reverse_lazy, reverse
from .models import Blog, Comment
from userauth.models import CustomUser
from userauth.forms import CustomUserUpdateForm

# Create your views here.

#views for blog
class BlogView(ListView):
    model = Blog
    template_name = 'core/main.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        model = self.model
        queryset = model.objects.order_by('-created_at')
        return queryset

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'core/blog-detail.html'
    context_object_name = 'blog'

    #add new context data to the template for the comment
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(blog = self.object)
        return context
    
    #add to ceate comment to the post
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object
            comment.user = self.request.user
            comment.save()
            return redirect('blog_detail', pk = self.object.pk)
        return self.get(request,*args,**kwargs)

class CreateBlogview(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'core/add-blog.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlogview,self).form_valid(form)

class UpdateBlogView(UpdateView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'core/update-blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('profile')

class DeleteBlogView(DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('profile')
    template_name = 'core/delete-blog.html'

class ViewBlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'core/view-detail-blog.html'




#views for profile
class ProfileView(ListView):
    model = Blog
    template_name = 'core/profile.html'
    context_object_name = 'blogs'

    def get_queryset(self):

        #get the id of the user
        pk = self.request.user.pk

        #get the user model
        User = get_user_model()

        #get the author
        author = User.objects.get(pk = pk)

        #fetch all the article of the author
        queryset = author.blog_posts.order_by('-created_at')

        return queryset

class UpdateProfileView(UpdateView):
    model = CustomUser
    context_object_name = 'user'
    form_class = CustomUserUpdateForm
    template_name = 'core/update-profile.html'
    success_url = reverse_lazy('profile')

