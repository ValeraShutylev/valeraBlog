from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from valeraBlog.apps.valeraBlogApp.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:  # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts})


def getpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/getpost.html', {'post': post})
