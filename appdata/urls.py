#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ricardo
@license: (C) Copyright 2018-2019 @yang.com Corporation Limited.
@contact: 659706575@qq.com
@software: made@Yang
@file: urls.py
@time: 2018/12/3 0003 10:59
@desc:
'''
from django.urls import path
from appdata import views
urlpatterns = [
    path('login/',views.login_port,name='login'),
    path('logic/',views.login_logic,name='logic'),
    path('show/',views.show,name='show'),

]