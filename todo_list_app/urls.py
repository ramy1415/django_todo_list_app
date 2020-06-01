from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Projects'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('showactive', views.show_active, name='show_active'),
    path('showdone', views.show_done, name='show_done'),
    path('additem', views.add_todo_item, name='add_todo_item'),
    path('togglestatus', views.toggle_status, name='toggle_status'),
]