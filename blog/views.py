from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    sentence = "This is the first django view thing I have done."
    return render(request, "index.html", {"sentence": sentence})


def why(request):
    why = "fun."
    return render(request, "why.html", {"why": why})

def show_post(request):
    post = Post.objects.all()
    return render(request, "post_list.html", {"post": post})