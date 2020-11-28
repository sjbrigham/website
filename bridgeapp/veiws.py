from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def blog_post_list_page(request):
    qs = BlogPost.objects.all()
    template_name = 'blog_list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)

def blog_post_detail_page(request, slug):
    obj = BlogPost.objects.get(slug=slug)
    template_name = 'blog_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)