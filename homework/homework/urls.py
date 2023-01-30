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
from django.urls import path, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from app.views import depart, user, pretty, admin, account, task, order, chart, upload, city

urlpatterns = [
    # 用户上传的文件存放的文件夹(方式一)
    # re_path(r"^media/(?P<path>.*)$",
    #         serve, {'document_root': settings.MEDIA_ROOT},
    #         name="media"),

    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录与注销
    path('login/', account.login),
    path('image/code/', account.image_code),
    path('logout/', account.logout),

    # 部门管理
    path('index/', depart.index),
    path('depart/list/', depart.derpat_list),
    path('depart/add/', depart.derpat_add),
    path('depart/delete/', depart.derpat_delete),
    # 通过url传值与使用？传值类似
    # /depart/number/edit/    中间必须得传值比如   /depart/4/edit/
    path('depart/<int:nid>/edit/', depart.derpat_edit),
    path('depart/multi/', depart.derpat_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/modelform/add/', user.user_modelform_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

    # 任务管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/edit/', order.order_edit),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/line/', chart.chart_line),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),

    # 文件上传
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modelform/', upload.upload_model_form),

    # 城市
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)  # 用户上传的文件存放的文件夹(方式二)
