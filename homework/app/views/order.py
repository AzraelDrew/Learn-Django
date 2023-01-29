from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app import models
import json
from datetime import datetime
from app.utils.form import OrderModelForm
from app.utils.pagination import Pagination

import random


def order_list(request):
    queryset = models.Order.objects.all().order_by("-id")
    form = OrderModelForm()
    page_object = Pagination(request, queryset)
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, "order_list.html", context)


# 创建订单
@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)

        # modelform在保存之前插入非用户提交的数据(或更改提交的数据)
        # form.instance.字段名 =  "xxxxxx"
        # 插入订单号
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # form.instance.price = 9999
        # 订单管理员为当前用户
        print(request.session["info"]["id"])
        form.instance.admin_id = request.session["info"]["id"]
        # 
        form.save()

        # 下面两行代码等价
        # return HttpResponse(json.dumps({"status":True}))
        return JsonResponse({"status": True})

    return JsonResponse({"status": False, "error": form.errors})


@csrf_exempt
def order_edit(request):
    # return HttpResponse("ok")
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "订单不存在,请刷新重试!!"})

    # 每个 ModelForm 也有 save() 方法。此方法根据绑定到表单的数据创建并保存数据库对象。
    # ModelForm 的子类可接受一个现有的模型实例作为关键字参数 instance ；
    # 如果提供了，则 save() 会更新这个实例。如果没有，则 save() 会创建一个对应模型的新实例
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


def order_delete(request):
    uid = request.GET.get("uid")
    # print(uid)
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败,订单不存在!"})
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    uid = request.GET.get("uid")
    print(uid)
    #   # 此方法获取到的是对象
    # row_object = models.Order.objects.filter(id = uid).first()
    #  获取的是一个字典   只包括values中的列
    row_object = models.Order.objects.filter(id=uid).values("title", "price", "status").first()
    print(row_object)

    # # 列表中套字典
    # row_dict  = models.Order.objects.all().values("id","title","price","status")
    # print(row_dict)
    # # 列表中套元组
    # row_yuanzu  = models.Order.objects.all().values_list("id","title","price","status")
    # print(row_yuanzu)

    if not row_object:
        return JsonResponse({{"status": False, "error": "数据不存在"}})

    result = {
        "status": True,
        # # row_object  为对象时的操作
        # "data":{
        # "title":row_object.title,
        # "price":row_object.price,
        # "status":row_object.status
        # }

        # 获取的数据为字典时
        "data": row_object
    }
    return JsonResponse(result)
