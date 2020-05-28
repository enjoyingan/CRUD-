from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title # 자기이름을 admin사이트 제목으로 보여주는 함수.