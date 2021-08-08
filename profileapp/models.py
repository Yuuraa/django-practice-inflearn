from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # Profile과 user 객체를 하나씩 연결해줌. 연결된 User 객체가 삭제될 때 어떻게 할 것인지 정책을 CASCADE로 설정함
    
    image = models.ImageField(upload_to='profile/', null=True) # 서버 내부 어디에 이미지를 저장할지, 그 경로. media/profile 아래에 저장될 것임
    nickname = models.CharField(max_length=20, unique=True, null=True) # 어떤 사람이든 고유의 닉네임을 갖도록
    message = models.CharField(max_length=100, null=True)

