from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),     # 여기에 다른 URL 패턴을 추가할 수 있습니다.
    path('home/', views.home, name='home'),  # 홈 페이지
    path('', views.login, name='login'),  # 기본 페이지는 로그인 페이지
]