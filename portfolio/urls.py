
from django.contrib import admin
from django.urls import path
from mypage import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]
