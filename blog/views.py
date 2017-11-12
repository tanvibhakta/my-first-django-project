from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User


def post_list(request):
    current = User.objects.get(username='almighty_author')
    posts = Post.objects.filter(author=current)

    return render(request, 'blog/template.html', { 'posts' : posts })
