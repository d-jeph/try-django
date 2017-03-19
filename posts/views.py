from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from  .models import Post
# Create your views here.
def post_list(request):
    queryset= Post.objects.all();
    context_data ={
    "post_list" : queryset,
    "title" : "List"
    }
    return render(request,"index.html",context_data);
def post_create(request):

    return HttpResponse("<h1>Create</h1>");

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    context_data ={
    "post": post,
    "title" : "Post "+ post.title
    }
    return render(request,"detail.html",context_data);


def post_update(request):

    return HttpResponse("<h1>update</h1>");
def post_delete(request):

    return HttpResponse("<h1>delete</h1>");