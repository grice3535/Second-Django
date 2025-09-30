from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    sentence = "This is the first django view thing I have done."
    return render(request, "index.html", {"sentence": sentence})


def why(request):
    why = "fun."
    return render(request, "why.html", {"why": why})

def show_post(request):
    post = Post.objects.all()
    return render(request, "post_lists.html", {"post": post})

def add_post(request):
    blogform = PostForm()
    if request.method == "POST": # if the submit button has been clicked
        blogform = PostForm(request.POST)
        if blogform.is_valid():
            blogform.save()
            return redirect("post")
    return render(request, "post_form.html", {"blogform": blogform})
 
def post_list(request):
    posts = Post.objects.filter(created_at=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})