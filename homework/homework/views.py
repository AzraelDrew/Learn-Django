from django.shortcuts import render,redirect
from app import models
# Create your views here.

def index(request):
    return render(request,"index.html")
# 部门列表 
def derpat_list(request):

    # 获取所有的部门
    queryset = models.Department.objects.all()

    return render(request,"depart_list.html",{"queryset":queryset})

# 添加部门
def derpat_add(request):
    if request.method == "GET":
        return render(request,"depart_add.html")
    # 获取用户通过POST提交的数据
    title = request.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向页面
    return redirect("/depart/list/")

# 删除部门
def derpat_delete(request):
    # 获取ID
    nid = request.GET.get("nid")
    # 删除部门
    models.Department.objects.filter(id=nid).delete()
    # 重定向
    return redirect("/depart/list/")

# 修改部门
def derpat_edit(request,nid):
    
    if request.method == "GET":
        # 查询当前部门名称
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id,row_object.title)
        return render(request,"depart_edit.html",{"title":row_object.title})
    if request.method =="POST":

        # 获取用户提交的部门名称
        # title = request.POST.get("title")
        title = request.POST["title"]
        # 更新部门名称
        models.Department.objects.filter(id = nid).update(title=title)
        return redirect("/depart/list/")
    
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
    return render(request,"user_list.html",{"queryset":queryset})

# 添加用户
def user_add(request):
    if request.method =="GET":
        context = {
            "gender_choices":models.UserInfo.gender_choices,
            "depart_list":models.Department.objects.all()
        }
        return render(request,"user_add.html",context)

    # 获取用户提交的数据
    user = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("ac")
    create_time = request.POST.get("create_time")
    gender_id = request.POST.get("gender")
    depart_id= request.POST.get("depart")
    # print(user,password,age,account,create_time,gender_id,depart_id) 
    models.UserInfo.objects.create(name=user,password = password,age = age,account = account,create_time = create_time,gender = gender_id,depart_id = depart_id)

    # 重定向
    return redirect("/user/list/")

# modelform 添加用户

from django import forms

# 用户信息modelform
class  UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3,label="用户名")
    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,item in self.fields.items():
            # 使用插件添加属性
            item.widget.attrs = {"class":"form-control","placeholder":item.label}

# 添加用户
def user_modelform_add(request):
    if request.method =="GET":
        form  = UserModelForm()
        return render(request,"user_modelform_add.html",{"form":form})

    # 提交数据
    form  = UserModelForm(data = request.POST)
    if form.is_valid():
        # 保存数据
        form.save()
        # 重定向
        return redirect("/user/list/")
    else:
        # 返回错误信息
        return render(request,"user_modelform_add.html",{"form":form})

# 编辑用户
def  user_edit(request,nid):
     #  根据ID获取需要编辑的数据
    row_obj  = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        #  instance = row_obj   # 当前编辑的数据
        form  = UserModelForm(instance = row_obj)
        return render(request,"user_edit.html",{"form":form})
    form = UserModelForm(data = request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return  render(request,"user_edit.html",{"form":form})

# 删除用户
def user_delete(request,nid):
    models.UserInfo.objects.filter(id = nid).delete()
    return redirect("/user/list/")

# 靓号列表
def pretty_list(request):
    # 搜索
    data_dict = {}
    search_value = request.GET.get("q","")
    if search_value:
        data_dict["mobile__contains"] = search_value

        # res = models.PrettyNumber.objects.filter(**data_dict)
        # print(res)
    # order_by("-level ")  表示  select * from  表 order by level desc;
    queryset = models.PrettyNumber.objects.filter(**data_dict).order_by("-level")   #  -  为desc     +  为asc
    
    return render(request,"pretty_list.html",{"queryset":queryset,"search_value":search_value})


# 靓号modelform
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class PrettyModelForm(forms.ModelForm):
    mobile = forms.CharField(label="手机号",
    validators=  [RegexValidator(r"^1[3-9]\d{9}$","手机号格式错误")])   # 字段校验规则   (方式一)
    class Meta:
        model = models.PrettyNumber
        fields = ['mobile','price','level','status']  #自定义字段
        # fields ="__all__"  #所有字段
        # exclude  = ['level']   #排除某个字段
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,item in self.fields.items():
            item.widget.attrs = {"class":"form-control","placeholder":item.label}

     # 字段校验规则   (方式二)  钩子函数
     # 函数名称clean_fields中的名称
    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNumber.objects.filter(mobile = text_mobile).exists()     #  是否存在返回bool值

        if exists:
            raise  ValidationError("手机号已存在")

        return text_mobile
            
# 编辑靓号时的 modelform
class PrettyEditModelForm(forms.ModelForm):
    # mobile = forms.CharField(disabled=True,label="手机号")   #不允许更改
    class Meta:
        model = models.PrettyNumber
        fields = ['mobile','price','level','status']  #自定义字段
        # fields ="__all__"  #所有字段
        # exclude  = ['level']   #排除某个字段
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,item in self.fields.items():
            item.widget.attrs = {"class":"form-control","placeholder":item.label}
    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNumber.objects.exclude(id=self.instance.pk).filter(mobile = text_mobile)    # exclude(id=number)   排除当前id的数据
        if exists:
            raise  ValidationError("手机号已存在") 

        return text_mobile
# 添加靓号
def pretty_add(request):
    if request.method =="GET":
        form = PrettyModelForm()
        return render(request,"pretty_add.html",{"form":form})
    form = PrettyModelForm(data = request.POST )
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    else:
        return render(request,"pretty_add.html",{"form":form})

def  pretty_edit(request,nid):
     #  根据ID获取需要编辑的数据
    row_obj  = models.PrettyNumber.objects.filter(id=nid).first()
    if request.method == "GET":
        #  instance = row_obj   # 当前编辑的数据
        form  = PrettyEditModelForm(instance = row_obj)
        return render(request,"pretty_edit.html",{"form":form})
    form = PrettyEditModelForm(data = request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return  render(request,"pretty_edit.html",{"form":form})

def pretty_delete(requestt,nid):
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")