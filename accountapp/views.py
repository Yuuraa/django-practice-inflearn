from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 브라우저에서 어떤 경로로 접속했을 때 보일 html 페이지를 만들 것

def hello_world(request):
    # return HttpResponse("Hell world!")
    return render(request, 'base.html')
