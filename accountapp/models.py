from django.db import models

# Create your models here.
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) #null을 사용해 이 attribute가 없어도 되는지 여부 지정
