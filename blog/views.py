from django.shortcuts import render

# Create your views here.

# 간단한 view를 만들어보자
def post_list(request):
    return render(request, 'blog/post_list.html', {})