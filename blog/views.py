from django.shortcuts import render, redirect
from .form import CreatePostForm, UpdatePostForm
from .models import Post

def CreatePostView(request):
    if request.method == 'POST':
        form =  CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-posts')
    else:
        form = CreatePostForm()
    context = {'form':form}
    return render(request, 'blog/create_post.html', context)

def UpdatePostView(request, pk):
    obj = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('all-posts')
    else:
        form = UpdatePostForm(instance=obj)
    context = {'form':form}
    return render(request, 'blog/update_post.html', context)

def PostDetailView(request, pk):
    obj = Post.objects.get(id=pk)
    context = {'obj':obj}
    return render(request, 'blog/post_detail.html', context)

def DeletePostView(request, pk):
    obj = Post.objects.get(id=pk)
    obj.delete()
    return redirect('all-posts')

