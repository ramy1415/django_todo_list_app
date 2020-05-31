from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Projects'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('additem', views.add_todo_item, name='home_page'),
]