from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.utils.form import TaskModelForm
from app import models
import json

from app.utils.pagination import Pagination


def task_list(request):
    queryset = models.Task.objects.all().order_by("-id")

    page_object = Pagination(request, queryset)
    form = TaskModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分页完都数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, "task_list.html", context)


@csrf_exempt  # 免除csrf_token认证
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    print("ajax")

    data_dict = {
        "statuc": True, "data": [11, 22, 33, 44]
    }
    # json_data = json.dumps(data_dict)   #  将python数据json化
    return HttpResponse(json.dumps(data_dict))


@csrf_exempt  # 免除csrf_token认证
def task_add(request):
    # print(request.POST)
    # 对用户发送的数据进行校验     

    form = TaskModelForm(data=request.POST)

    if form.is_valid():
        form.save()
        data_dict = {
            "status": True
        }
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
