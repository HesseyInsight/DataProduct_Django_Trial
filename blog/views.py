from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

# 간단한 view를 만들어보자
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})



def img_search(request, img_id):
    google_url = 'www.ggl.~~'
    total_url = google_url + img_id
    return redirect(total_url)
    pass
# models.py파일에 정의된 모델을 가져올 것이다. 
# 다음 step에서 QuerySet을 Template에 보내는 방법을 배워보도록 한다.

# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')