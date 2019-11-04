from django.contrib import admin
from .models import Post  # 앞서 만든 Post 모델을 import 한다.

admin.site.register(Post)  # 관리자 페이지에서 만든 모델을 보려면 admin.site.register(Post)로 모델을 등록해야 한다.
