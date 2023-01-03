"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),


    # 部门管理
    path('index/', views.index),
    path('depart/list/', views.derpat_list),
    path('depart/add/', views.derpat_add),
    path('depart/delete/', views.derpat_delete),
    # 通过url传值与使用？传值类似
    # /depart/number/edit/    中间必须得传值比如   /depart/4/edit/
    path('depart/<int:nid>/edit/', views.derpat_edit),


    # 用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/modelform/add/', views.user_modelform_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),


    # 靓号管理
    path('pretty/list/',views.pretty_list),
    path('pretty/add/',views.pretty_add),
    path('pretty/<int:nid>/edit/', views.pretty_edit),
    path('pretty/<int:nid>/delete/', views.pretty_delete),


]