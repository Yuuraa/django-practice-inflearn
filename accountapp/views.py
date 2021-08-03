from django.shortcuts import render
from django.http import HttpResponse

from accountapp.models import HelloWorld

# 브라우저에서 어떤 경로로 접속했을 때 보일 html 페이지를 만들 것
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_data = HelloWorld()
        new_hello_data.text = temp
        new_hello_data.save() # DB에 객체 저장

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_data})

    return render(request, 'accountapp/hello_world.html')
