from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic.base import TemplateResponseMixin

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, PasswordUpdateView, AccountDeleteView


app_name = 'accountapp' # 이걸 써주어서 hello world 경로에 접근을 했을 때 accountapp:hello_world 이런 식으로 쓸 수 있게 됨

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    
    path('login/', LoginView.as_view(template_name="accountapp/login.html"), name='login'), # LoginView는 template을 지정해 주어야 함
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('create/', AccountCreateView.as_view(), name='create'), # 클래스형은 이런 식으로 가져와야 함
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),  # 특정 유저 개체에 부여된 고유한 키가 필요함
    path('update/<int:pk>', PasswordUpdateView.as_view(), name='update'),  # 특정 유저 개체에 부여된 고유한 키가 필요함
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),  # 특정 유저 개체에 부여된 고유한 키가 필요함
]
