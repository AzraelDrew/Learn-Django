from django.shortcuts import render, redirect, HttpResponse
from app import models
from app.utils.form import LoginForm
from app.utils.code import check_code
""" 登录与注销管理 """


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功后提交的数据
        # print(form.cleaned_data)

        # Form与ModelForm
        # Form没有  form.save()方法   因为ModelFrom是关联数据库的而Form没有

        # 验证码的校验
        # 将code弹出而不是获取     因为在数据库中没有code这一字段
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get("image_code", "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, "login.html", {"form": form})
        # 数据库校验用户名和密码
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "密码或用户名错误")
            return render(request, "login.html", {"form": form})

        # 用户名和密码正确
        # 网站生成随机字符串;写到用户浏览器的cookie中;再写入到session中;
        # 随机字符串存储在浏览器的cookie中和数据库的django_session中
        request.session["info"] = {
            "id": admin_object.id,
            "name": admin_object.username
        }
        # 登录信息可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)

        return redirect("/admin/list/")

    return render(request, "login.html", {"form": form})


from io import BytesIO


def image_code(request):
    img, code_str = check_code()

    #  将图片验证码保存到session中 (以便于后续获取验证码再进行校验)
    request.session["image_code"] = code_str
    # 给session设置60s超时
    request.session.set_expiry(60)
    print(check_code)

    stream = BytesIO()
    img.save(stream, "png")
    # src =  stream.getvalue()
    # print(src)
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.clear()  # 清楚当前用户的session与cookie
    return redirect("/login/")
