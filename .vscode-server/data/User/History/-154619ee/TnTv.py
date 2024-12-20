from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),     # 여기에 다른 URL 패턴을 추가할 수 있습니다.
    path('', views.home),
    path('logout/', views.logout),   # 홈 페이지
]