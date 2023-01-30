from django.shortcuts import render, redirect
from app import models
from app.utils.form import UpModelForm


def city_list(request):
    queryset = models.City.objects.all()

    return render(request, "city_list.html", {"queryset": queryset})


def city_add(request):

    title = "添加城市"
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, "upload_form.html", {
            "title": title,
            "form": form
        })
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 自动保存文件
        # 字段会自动写入数据库
        form.save()

        return redirect("/city/list/")
    return render(request, "upload_form.html", {"title": title, "form": form})