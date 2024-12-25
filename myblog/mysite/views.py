from django.shortcuts import render ,redirect
from django.http import HttpResponse # type: ignore
from mysite.models import Post
from datetime import datetime
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now=datetime.now()
    # post_lists =list()
    # for count,post in enumerate(posts):
    #     post_lists.append(f"No.{count} {post} <br>")
    return render(request,"index.html",locals())

def showpost(request,slug): 
    try:
        post=Post.objects.get(slug=slug)
        if post!=None:
            return render(request,"post.html",locals()) 
    except:
        #有問題回首頁
        return redirect('/')