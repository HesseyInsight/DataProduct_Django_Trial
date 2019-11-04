from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):  # 모델을 정의하는 코드(모델은 객체(object)다?!)
                           # class-객체, Post-모델의 이름, models-Post가 장고 모델임을 의미한다.

    # 이하 속성
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # 글자 수가 제한된 텍스트 정의
    text = models.TextField()  # 글자수 제한이 없는 긴 텍스트, 본문(콘텐츠)에 적합
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    # 이하 메서드:: publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    