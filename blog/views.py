from django.shortcuts import render
from django.utils import timezone
from .models import Post
#마침표(.)는 현재 디렉토리에 있는 파일
#Post모델에서 블로그 글을 가져오기 위해서는 쿼리셋(QuerySet)이 필요하다.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
