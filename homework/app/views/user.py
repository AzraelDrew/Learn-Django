from django.shortcuts import render, redirect
from django.core.validators import RegexValidator  # 正则验证
from django.core.exceptions import ValidationError  # 规则验证报错
from app import models  # 数据库
from app.utils.pagination import Pagination  # 分页组件(实现)
from app.utils.form import UserModelForm  # BootStrap   ModelForm  样式
"""  用户管理 """


# 用户列表
def user_list(request):
    # 获取所有的用户
    queryset = models.UserInfo.objects.all()
    # print(queryset)
    # for obj in queryset:
    #     print(obj.id,obj.name,obj.password,obj.age,obj.account,obj.create_time.strftime("%Y-%m-%d"),obj.gender,obj.get_gender_display(),obj.depart_id,obj.depart.title)

    #     # print(obj.get_gender_display())     #  会将对应数值的对应值输出    格式  obj.get_字段名_display
    #     # obj.depart_id    # 获取数据库中存储的值

    # obj.depart.title   #  很据ID自动去关联的表中查找数据    obj.字段名.列名
    page_object = Pagination(request, queryset, page_size=2)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, "user_list.html", context)


# 添加用户
def user_add(request):
    if request.method == "GET":
        context = {
            "gender_choices": models.UserInfo.gender_choices,
            "depart_list": models.Department.objects.all()
        }
        return render(request, "user_add.html", context)

    # 获取用户提交的数据
    user = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("ac")
    create_time = request.POST.get("create_time")
    gender_id = request.POST.get("gender")
    depart_id = request.POST.get("depart")
    # print(user,password,age,account,create_time,gender_id,depart_id)
    models.UserInfo.objects.create(name=user,
                                   password=password,
                                   age=age,
                                   account=account,
                                   create_time=create_time,
                                   gender=gender_id,
                                   depart_id=depart_id)

    # 重定向
    return redirect("/user/list/")


# 添加用户
def user_modelform_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_modelform_add.html", {"form": form})

    # 提交数据
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 保存数据
        form.save()
        # 重定向
        return redirect("/user/list/")
    else:
        # 返回错误信息
        return render(request, "user_modelform_add.html", {"form": form})


# 编辑用户
def user_edit(request, nid):
    #  根据ID获取需要编辑的数据
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        #  instance = row_obj   # 当前数据库中的的数据
        form = UserModelForm(instance=row_obj)
        return render(request, "user_edit.html", {"form": form})
    form = UserModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})


# 删除用户
def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
