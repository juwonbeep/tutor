from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),  # 여기에 다른 URL 패턴을 추가할 수 있습니다.
]