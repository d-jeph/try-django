from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    queryset= Post.objects.all();
    context_data ={
    "post_list" : queryset,
    "title" : "List"
    }
    return render(request,"posts.html",context_data);

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Post created successfully")
        return HttpResponseRedirect(instance.get_absolute_url())

    context_data = {
        "form":form,
        "title" : "New Post",
    }
    return render(request,"post_form.html",context_data);

def post_detail(request,id=None):
    post = get_object_or_404(Post,id=id)
    context_data ={
    "post": post,
    "title" : "Post "+ post.title
    }
    return render(request,"detail.html",context_data);


def post_update(request,id=None):
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #add some messag here
        messages.success(request,"Post saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.success(request,"An error occured")
 
    context_data ={
    "post": instance,
    "title" : instance.title,
    "form": form,
    }
    return render(request,"post_form.html",context_data);

def post_delete(request,id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Post deleted")
    return redirect("posts:list");