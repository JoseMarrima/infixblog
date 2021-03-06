from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]