from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp' # 이걸 써주어서 hello world 경로에 접근을 했을 때 accountapp:hello_world 이런 식으로 쓸 수 있게 됨

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'), # 클래스형은 이런 식으로 가져와야 함
]
