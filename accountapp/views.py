from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accountapp.models import HelloWorld
from .forms import PasswordUpdateForm


# 브라우저에서 어떤 경로로 접속했을 때 보일 html 페이지를 만들 것
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_data = HelloWorld()
        new_hello_data.text = temp
        new_hello_data.save() # DB에 객체 저장
        
        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'

class PasswordUpdateView(UpdateView):
    model = User
    form_class = PasswordUpdateForm
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:hello_world')
    context_object_name = 'target_user'

class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:login')
    context_object_name = 'target_user'