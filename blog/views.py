from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.
def blogHome(request):
    allposts =Post.objects.all()
    context={'allposts':allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request):
    allposts =Post.objects.all()
    context={'allposts':allposts}
    return render(request,'blog/blogPost.html',context)

