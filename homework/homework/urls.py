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
from django.urls import path
from app.views import depart,user,pretty


urlpatterns = [

    # 部门管理
    path('index/', depart.index),
    path('depart/list/', depart.derpat_list),
    path('depart/add/', depart.derpat_add),
    path('depart/delete/', depart.derpat_delete),
    # 通过url传值与使用？传值类似
    # /depart/number/edit/    中间必须得传值比如   /depart/4/edit/
    path('depart/<int:nid>/edit/', depart.derpat_edit),


    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/modelform/add/', user.user_modelform_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),


    # 靓号管理
    path('pretty/list/',pretty.pretty_list),
    path('pretty/add/',pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

]   