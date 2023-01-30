from django.shortcuts import render, HttpResponse
from app.utils.form import UpForm, UpModelForm
from app import models
import os


def upload_list(request):
    if request.method == "GET":
        return render(request, "upload_list.html")
    print(request.POST)  # 请求体中的数据
    print(request.FILES)  # 请求发送过来的文件

    file_object = request.FILES.get("avatar")
    print(file_object.name)
    print(file_object)
    f = open(file_object.name, mode="wb")
    for chunk in file_object.chunks():
        f.write(chunk)

    f.close()
    return HttpResponse("...")


def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, "upload_form.html", {
            "title": title,
            "form": form
        })
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        print(form.cleaned_data)

        # 读取内容,处理每个字段的数据
        # 读取图片内容,写入到文件夹中并获取文件路径
        image_object = form.cleaned_data.get("img")
        from django.conf import settings
        # media_path = os.path.join(settings.MEDIA_ROOT, image_object.name)   # 此方法为绝对路径
        media_path = os.path.join("media", image_object.name)  #  此方法为相对路径

        print(media_path)

        f = open(media_path, mode="wb")
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        # 将文件路径写入到数据库
        models.Boos.objects.create(name=form.cleaned_data['name'],
                                   age=form.cleaned_data['age'],
                                   img=media_path)
        return HttpResponse("...")
    return render(request, "upload_form.html", {"title": title, "form": form})


def upload_model_form(request):
    title = "ModelForm上传"
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
        # 如果上传的文件同名Django会自动重命名

        form.save()

        return HttpResponse("...")
    return render(request, "upload_form.html", {"title": title, "form": form})