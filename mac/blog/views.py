from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.
def index(request):
  mypost = BlogPost.object.all()
  return render(request,'blog/index.html',{"mypost":mypost})
def blogpost(request,id):

  post = BlogPost.object.filter(post_id=id)[0]
  return render(request,'blog/blogpost.html',{"post":post})