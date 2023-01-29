from django.shortcuts import render, redirect
from app import models  # 数据库
from app.utils.pagination import Pagination  # 分页组件(实现)
from app.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm


# 管理员列表
def admin_list(request):
    # # 在视图函数中实现鉴权
    # # 检查用户是否已经登录    若未登陆则返回登录页面
    # # 获取浏览器中的cookie随机字符串
    # info = request.session.get("info")
    # print('info',info)
    # if not info :
    #     return redirect("/login/") 

    data_dict = {}
    search_value = request.GET.get("q", "")
    if search_value:
        data_dict["username__contains"] = search_value
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分页完都数据
        "page_string": page_object.html(),  # 生成页码
        "search_value": search_value,

    }
    return render(request, "admin_list.html", context)


# t添加管理员
def admin_add(request):
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "add_and_edit.html", {"title": title, "form": form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        clean_data = form.cleaned_data  # 验证通过后的所有信息
        if clean_data["password"] == clean_data["confirm_password"]:
            form.save()
            return redirect("/admin/list/")
    return render(request, "add_and_edit.html", {"title": title, "form": form})


# 编辑管理员
def admin_edit(request, nid):
    title = "编辑管理员"
    row_object = models.Admin.objects.filter(id=nid).first()
    if request.method == "GET":
        if not row_object:
            return redirect("/admin/list/")
        form = AdminEditModelForm(instance=row_object)
        return render(request, "add_and_edit.html", {"title": title, "form": form})
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "add_and_edit.html", {"title": title, "form": form})


# 删除管理员
def admin_delete(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")


# 重置密码
def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        if not row_object:
            return redirect("/admin/list/")

        form = AdminResetModelForm()
        return render(request, "add_and_edit.html", {"title": title, "form": form})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "add_and_edit.html", {"title": title, "form": form})
