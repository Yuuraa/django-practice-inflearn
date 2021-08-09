from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView(template_name='articleapp/list.html'), name='list'),
]
