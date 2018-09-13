from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
# Create your views here.
from .models import Post,Category
from django.utils.timezone import now

def index(request):
    rank_1=Post.objects.rank_1()
    recent_post=Post.objects.all().order_by('-date')[:3]
    categories=Category.objects.all()
    dictionary = {}
    for category in categories:
        post_list=Post.objects.filter(category=category).order_by('-date')[:4]
        dictionary[category]=post_list
    popular_post=Post.objects.filter(rating='3').order_by('date')[:5]
    trending_post=Post.objects.filter(rating='4').order_by('date')[:5]
    return render(request, 'post/index.html',{'now':now(),'rank_1':rank_1,'recent_post':recent_post,
                                              'dictionary':dictionary,'popular_post':popular_post,
                                              'trending_post':trending_post})

def post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'post/single_center.html',{'now':now(),'post':post})

def category(request):
    return render(request, 'post/category_three.html')
