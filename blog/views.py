from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag, Author
#=====================================================================================
def starting_page(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })
#=====================================================================================
def posts(request):
    all_posts = Post.objects.order_by('-date')
    return render(request, "blog/posts.html", {
        "posts": all_posts
    })
#=====================================================================================
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": post
    })
#=====================================================================================
def page_not_found_view(request, exception):
    return render(request, "404.html", status=404)
#=====================================================================================
def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors_list.html', {'authors': authors})
#=====================================================================================
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    posts = Post.objects.filter(author=author).order_by('-date')
    return render(request, 'blog/author_detail.html', {'author': author, 'posts': posts})
#=====================================================================================
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})
#=====================================================================================
def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = Post.objects.filter(tags=tag).order_by('-date')
    return render(request, 'blog/tag_detail.html', {'tag': tag, 'posts': posts})
