import re
from django.shortcuts import render,HttpResponse
from home.models import Contact
from blog.models import Post
# Create your views here.
def home(request):
    allposts =Post.objects.all()
    context={'allposts':allposts}
    return render(request, 'home/home.html',context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        stream=request.POST.get('stream')
        concern=request.POST.get('concern')
        print(name, email, phone, stream)
        contact=Contact(name=name, email=email, phone=phone,stream=stream,concern=concern)
        contact.save()
    return render(request, 'home/contact.html')

def login(request):
    return render(request, 'home/login.html')