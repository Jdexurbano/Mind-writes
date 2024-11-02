from django.db import models
from userauth.models import CustomUser
# Create your models here.

#model for the blog
class Blog(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name='blog_posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.author} {self.title}"


#model for the comment
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name='blog_comments')
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name='commenter')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.blog} {self.user} {self.content}")
