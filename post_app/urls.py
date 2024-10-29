from django.urls import path
from .import views

# 순서3 - 브라우저에서 들어온 url패턴을 확인해서 views.py에 있는 함수 호출
# 주소창에 localhost:8000/posts라는 요청이 들어오면 아래 url패턴이 인지해서 views.py에 있는 posts 함수 실행
urlpatterns = [
  path('posts', views.posts, name='posts'),
  path('posts/<slug:slug>/', views.posts_detail, name='post-detail'),
  path("posts-search/", views.posts_search, name='posts-search')
]