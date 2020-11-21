#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path

from App import views

# 路由列表
urlpatterns = [
    # 不能以/开头
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login')
]
