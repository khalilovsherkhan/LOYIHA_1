from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    post = Post.objects.all()
    context = {
        'post':post

    }
    return render(request,'index.html', context)

def post_detail(request, pk):
    data = get_object_or_404(Post, pk=pk)
    context = {
        'data':data
    }
    return render(request, 'post_detail.html', context)