from django.shortcuts import render
from blog.models import Article, Tag
 
def home(request):
    post_list = Article.objects.all()
 
    return render(request, 'blog/index.html', {'post_list':post_list})

def get_articles(request, tag_name):
    posts = Article.objects.filter(tag__tag_name = tag_name)
 
    return render(request, 'blog/index.html', {'post_list':post_list})    

def detail(request, id):
    post = Article.objects.get(id = str(id))
    return render(request, 'blog/detail.html', {'post':post})    