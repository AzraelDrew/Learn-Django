from django.core.validators import RegexValidator  # 正则验证
from django.core.exceptions import ValidationError  # 规则验证报错
from django import forms  # form组件(django)
from app import models  # 数据库
from app.utils.bootstrap import BootStrapModelForm, BootStrapForm  # BootStrap   ModelForm  样式
from app.utils.encrypt import md5
""" Form与ModelForm """


# modelform 添加用户
#    用户信息modelform
class UserModelForm(BootStrapModelForm):
    #class  classname(BootStrapModelForm):      继承BootStrap样式

    name = forms.CharField(min_length=2, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = [
            'name', 'password', 'age', 'account', 'create_time', 'gender',
            'depart'
        ]


# 编辑靓号时的 modelform
class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True,label="手机号")   #不允许更改
    class Meta:
        model = models.PrettyNumber
        fields = ['mobile', 'price', 'level', 'status']  #自定义字段
        # fields ="__all__"  #所有字段
        # exclude  = ['level']   #排除某个字段
    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNumber.objects.exclude(
            id=self.instance.pk).filter(
                mobile=text_mobile)  # exclude(id=number)   排除当前id的数据
        # print('number', self.instance.mobile)
        # print('price', self.instance.price)
        # print('level', self.instance.level)
        # print('status', self.instance.status)
        # print('id', self.instance.id)
        # print('pk', self.instance.pk)
        if exists:
            raise ValidationError("手机号已存在")
        return text_mobile


# 靓号modelform
class PrettyModelForm(BootStrapModelForm):
    mobile = forms.CharField(
        label="手机号", validators=[RegexValidator(r"^1[3-9]\d{9}$",
                                                "手机号格式错误")])  # 字段校验规则   (方式一)

    class Meta:
        model = models.PrettyNumber
        fields = ['mobile', 'price', 'level', 'status']  #自定义字段
        # fields ="__all__"  #所有字段
        # exclude  = ['level']   #排除某个字段

    # 字段校验规则   (方式二)  钩子函数
    # 函数名称clean_fields中的名称
    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNumber.objects.filter(
            mobile=text_mobile).exists()  #  是否存在返回bool值
        if exists:
            raise ValidationError("手机号已存在")
        return text_mobile


# 新建管理员


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        # 插件
        widgets = {
            # render_value=True 不会清空输入框
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        print(confirm)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm  # return 返回的是保存到数据库中的值


# 编辑管理员
class AdminEditModelForm(BootStrapModelForm):

    class Meta:
        model = models.Admin
        fields = ["username"]


# 重置管理员密码
class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码", widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        # 插件
        widgets = {
            # render_value=True 不会清空输入框
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        print('edit', self.cleaned_data.get("password"))
        pwd = self.cleaned_data.get("password")
        print(self.cleaned_data.get("confirm_password"))
        confirm = md5(self.cleaned_data.get("confirm_password"))
        print('current', confirm)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        exists = models.Admin.objects.filter(id=self.instance.pk,
                                             password=pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")
        return confirm  # return 返回的是保存到数据库中的值


class LoginForm(BootStrapForm):  # 直接继承BootStrapForm
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "用户名"
        }),
        required=True  # 必填项  不能为空
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "密码"
        },
                                   render_value=True),
        required=True,  # 必填项  不能为空
    )

    code = forms.CharField(label="验证码", widget=forms.TextInput, required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    # 使用上面与下面的方式是同样都效果  或者直接继承BootStrapForm

    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for name,item in self.fields.items():
    #         # 此方法会将原有的属性覆盖
    #         # item.widget.attrs = {"class":"form-control","placeholder":item.label}

    #         # 保留原来都属性,若没有属性则添加属性
    #         if item.widget.attrs:
    #             item.widget.attrs["class"] = "form-control"
    #             item.widget.attrs["placeholder"] = item.label
    #         else:
    #             item.widget.attrs = {"class":"form-control","placeholder":item.label}


class TaskModelForm(BootStrapModelForm):

    class Meta:
        model = models.Task
        # fields = ["level","title"]
        fields = "__all__"


class OrderModelForm(BootStrapModelForm):

    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["oid", "admin"]


class UpModelForm(BootStrapModelForm):

    class Meta:
        model = models.City
        fields = "__all__"


class UpForm(BootStrapForm):
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")