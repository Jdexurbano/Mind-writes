from django.urls import path,include
from .views import BlogView,BlogDetailView,CreateBlogview,ProfileView,UpdateBlogView,DeleteBlogView,UpdateProfileView,ViewBlogDetail
urlpatterns = [
    path('auth/',include('userauth.urls')),
    path('',BlogView.as_view(),name='main'),
    path('article/<int:pk>',BlogDetailView.as_view(),name='blog_detail'),
    path('create/article/',CreateBlogview.as_view(),name='create_blog'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/update/<int:pk>',UpdateProfileView.as_view(),name='update_profile'),
    path('update/aritcle/<int:pk>',UpdateBlogView.as_view(),name='update_blog'),
    path('delete/article/<int:pk>',DeleteBlogView.as_view(),name='delete-blog'),
    path('view/article/<int:pk>',ViewBlogDetail.as_view(),name='view_blog'),

]