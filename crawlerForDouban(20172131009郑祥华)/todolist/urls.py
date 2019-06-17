from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home,name="主页"),
    path('about/', views.about,name="关于"),
    path('suibi/', views.suibi,name="随笔"),
    path('shige/', views.shige,name="诗歌"),
    path('xiaoshuo/', views.xiaoshuo,name="小说"),
]