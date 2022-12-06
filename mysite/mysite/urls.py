"""mysite URL Configuration

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
# from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),  #django提高的默认后台管理
    path('index/',views.index),  #当访问index这个url(路由)时就会去views.py中找到index这个函数并执行 
    
    path('user/list/',views.user_list),

    path('user/add/',views.user_add),

    path('template_syntax/',views.template_syntax),

    # 伪联通新闻中心
    path('news/',views.news),

    # 请求和响应
    path('something/',views.something),

    # 用户登录
    path('login/',views.login),
]