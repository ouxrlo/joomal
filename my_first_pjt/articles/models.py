## DB관련 데이터 정의 파일

from django.db import models

class Aritcles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()