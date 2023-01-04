from django.shortcuts import render,redirect           
from django.core.validators import RegexValidator      # 正则验证
from django.core.exceptions import ValidationError     # 规则验证报错  
from app import models                                 # 数据库  
from django import forms                               # form组件(django)
from app.utils.pagination import Pagination            # 分页组件(实现)

# Create your views here.

def index(request):
    return render(request,"index.html")
# 部门列表 
def derpat_list(request):

    # 获取所有的部门
    queryset = models.Department.objects.all()
    page_object = Pagination(request,queryset,page_size=2)
    context = {
        "queryset":page_object.page_queryset,
        "page_string":page_object.html()
    }
    return render(request,"depart_list.html",context)

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
    page_object = Pagination(request,queryset,page_size=2)
    context = {
        "queryset":page_object.page_queryset,
        "page_string":page_object.html()
    }
    return render(request,"user_list.html",context)

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
#    用户信息modelform
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

    # for i in range(300):
    #     models.PrettyNumber.objects.create(mobile = "18188888888",price=88,level=2,status=3)
    # 搜索
    data_dict = {}
    search_value = request.GET.get("q","")
    if search_value:
        data_dict["mobile__contains"] = search_value

    # models.PrettyNumber.objects.filter(price = 88).delete()

#     # 分页
#     page = int(request.GET.get("page",1))
#     page_size = 10   # 没页大小 
#     start = (page - 1) * page_size
#     end = page * page_size

#     # order_by("-level ")  表示  select * from  表 order by level desc;    
#     queryset = models.PrettyNumber.objects.filter(**data_dict).order_by("id")[start:end]   #  -  为desc     +  为asc
    
#     totle_count= models.PrettyNumber.objects.filter(**data_dict).count() # 符合条件的数据共有多少条
#     totle_page_count,div = divmod(totle_count,page_size)
#     if div:
#         totle_page_count+=1
#     plus=8
#     # 数据较少时
#     if totle_page_count<= 2*plus+1:
#         start_page =1
#         end_page = totle_page_count
#     # 数据较多时
#     else:
#         # 当前小于5页
#         if page<=plus:
#             start_page =1
#             end_page = 2*plus+1
#         else:
#             # 当前页+5大于总页面
#             if (page+plus)>totle_page_count:
#                 start_page =totle_page_count-2*plus
#                 end_page = totle_page_count
#             else:
#                 start_page = page-plus
#                 end_page = page+plus

#     #  页码
#     page_str_list=[]

#     # 首页
#     page_str_list.append("<li><a href='?page={}'>首页</a></li>".format(1))

#     # 上一页
#     if page>1:
#         prev = "<li><a href='?page={}'>上一页</a></li>".format(page-1)
#     else:
#         prev = "<li><a href='?page={}'>上一页</a></li>".format(1)
#     page_str_list.append(prev)


#     for i in range(start_page,end_page+1 ):
#         if i==page:
#             ele = "<li class='active' ><a href='?page={}'>{}</a></li>".format(i,i)
#         else:
#             ele = "<li><a href='?page={}'>{}</a></li>".format(i,i)

#         page_str_list.append(ele)


#     # 下一页
#     if page<totle_page_count:
#         next = "<li><a href='?page={}'>下一页</a></li>".format(page+1)
#     else:
#         next = "<li><a href='?page={}'>下 一页</a></li>".format(totle_page_count)
#     page_str_list.append(next)

#     # 尾页
#     page_str_list.append("<li><a href='?page={}'>尾页</a></li>".format(totle_page_count))

#     search_string = """    <li>  
#       <form method="GET" >
#       <div class="input-group">
#         <input type="text" name="page" class="form-control" placeholder="页码" style="border-radius: 0;"/>
#         <span class="input-group-btn">
#           <button class="btn btn-default" type="submit" style="border-radius: 0;">
#           跳转</button>
#           </button>
#         </span> 
#       </div>
#     </form>
#   </li>"""
#     page_str_list.append(search_string)
#     page_string = mark_safe("".join(page_str_list))
    # context ={
    #     "queryset":queryset,
    #     "search_value":search_value,
    #     "page_string":page_string
    # }


    # class分页

    queryset = models.PrettyNumber.objects.filter(**data_dict).order_by("id")
    page_object = Pagination(request,queryset  )
    context ={
        "queryset":page_object.page_queryset,
        "search_value":search_value,
        "page_string":page_object.html()
    }

    return render(request,"pretty_list.html",context)

# 靓号modelform
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