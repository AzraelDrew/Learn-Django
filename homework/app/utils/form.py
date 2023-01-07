from django.core.validators import RegexValidator                       # 正则验证
from django.core.exceptions import ValidationError                      # 规则验证报错  
from app import models                                                  # 数据库  
from django import forms                                                # form组件(django)
from app.utils.bootstrap_modelform import BootStrapModelForm            # BootStrap   ModelForm  样式

# modelform 添加用户
#    用户信息modelform
class  UserModelForm(BootStrapModelForm):    #class  classname(BootStrapModelForm):      继承BootStrap样式
    name = forms.CharField(min_length=3,label="用户名")
    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']
# 编辑靓号时的 modelform
class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True,label="手机号")   #不允许更改
    class Meta:
        model = models.PrettyNumber
        fields = ['mobile','price','level','status']  #自定义字段
        # fields ="__all__"  #所有字段
        # exclude  = ['level']   #排除某个字段
    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNumber.objects.exclude(id=self.instance.pk).filter(mobile = text_mobile)    # exclude(id=number)   排除当前id的数据
        if exists:
            raise  ValidationError("手机号已存在") 
        return text_mobile

# 靓号modelform
class PrettyModelForm(BootStrapModelForm):
    mobile = forms.CharField(label="手机号",
    validators=  [RegexValidator(r"^1[3-9]\d{9}$","手机号格式错误")])   # 字段校验规则   (方式一)
    class Meta:
        model = models.PrettyNumber
        fields = ['mobile','price','level','status']  #自定义字段
        # fields ="__all__"  #所有字段
        # exclude  = ['level']   #排除某个字段

     # 字段校验规则   (方式二)  钩子函数
     # 函数名称clean_fields中的名称
    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNumber.objects.filter(mobile = text_mobile).exists()     #  是否存在返回bool值
        if exists:
            raise  ValidationError("手机号已存在")
        return text_mobile