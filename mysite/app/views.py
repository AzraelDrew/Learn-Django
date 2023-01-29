from django.shortcuts import render,HttpResponse,redirect
from app.models import UserInfo,Deparment

# Create your views here.
def index(request):   #request为默认参数   是一个对象,封装了用户发送过来的所有数据
    return HttpResponse("欢迎使用!")
    #如若需要在根目录下查找则需要在setting.py中的TEMPLATES踪添加'DIRS': [os.path.join(BASE_DIR,"templates")]
    #若根目录下没有找到对应的html文件
    #则会根据app的注册顺序去/appname/templates/下找user_list.html并返回(若没有配置根目录则默认在app中查找)
def user_list(request):
    return render(request,'user_list.html')   

def user_add(request):
    return render(request,"user_add.html")

def template_syntax(request):
    name = "Azrael"
    roles = ["admin","CEO","保安"]
    user_info = {"name":"azrael","salary":100000,"role":"CTO"}

    data_list = [

        {"name":"azrael","salary":100000,"role":"CTO"},
        {"name":"alex","salary":140000,"role":"CO"},
        {"name":"drew","salary":190000,"role":"CEO"}
    ]
    return render(request,"template_syntax.html",{"n1":name,"n2":roles,"n3":user_info,"n4":data_list})

# 伪联通新闻中心
def news(req):
    #在网络上获取数据
    #向  http://www.chinaunicom.com/api/article/NewsByIndex/2/2021/12/news 发送请求
    #利用第三方模块:requests
    import requests
    url = "http://www.chinaunicom.com/api/article/NewsByIndex/2/2022/11/news"
    res=requests.get(url,headers={"User-Agent": "XY"})
    data_list = res.json()
    # print(res)
    # print(data_list)
    return render(req,'news.html',{"news_list":data_list})

# 请求和响应
def something(request):

    # [请求] 获取请求方式  GET/POST
    print(request.method)

    # [请求]  在url上传值   /something/?n1=123&n2=999
    # 获取url传递过来的参数
    print(request.GET)   # {'n1': ['123'], 'n2': ['999']}

    # [请求]  获取请求体中提交的数据
    print(request.POST)

    # [响应] 返回内容给请求者 可以是字符串或者json数据
    # return HttpResponse("返回内容")

    # [响应] 读取HTML的内容 + 渲染 -> 字符串返回给用户浏览器
    # return render(request,"something.html",{"title":"来了"})

    # [响应] 重定向到其他页面
    return redirect('http://www.baidu.com')

# 用户登录
def login(request):

    if(request.method=='GET'):
        return render(request,"login.html")

    # 以下两张方法都能获取到POST中的数据
    print(request.POST["user"])
    print(request.POST["pwd"])
    print(request.POST.get("user"))
    print(request.POST.get("pwd"))

    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username=="admin" and password=="yznaisy":
        # return HttpResponse("登录成功")
        return redirect('http://www.chinaunicom.com/')
    # return HttpResponse("登录失败")
    return render(request,"login.html",{"error_msg":"用户名或密码错误"})

# ORM
def orm(request):
        #测试ORM操作表中的数据
        # ### 1.新建 ###
        # Deparment.objects.create(title="销售部")
        # Deparment.objects.create(title="IT部")
        # Deparment.objects.create(title="运营部")

        # UserInfo.objects.create(name="Azrael",password="123",age=19)
        # UserInfo.objects.create(name="Alex",password="666",age=29)
        # UserInfo.objects.create(name="drew",password="666")

        # object = UserInfo(name="test",password="123",age=22)
        # object.save()


        # ### 2.删除 ###
        # UserInfo.objects.filter(age=2).delete()   #删除age=2的数据
        # Deparment.objects.all().delete()   #删除所有数据

        # ### 3.获取数据 ###
        # Querset = [obj,obj,obj]    一个列表中有多个对象
        # QuerySet =  UserInfo.objects.all()   #获取当前表的所有数据
        # print(QuerySet)

        # for obj in QuerySet:
        #     print(obj.id,obj.name,obj.password,obj.age)

        # QuerySet = UserInfo.objects.filter(age=29)
        # print(QuerySet)
        # for obj in QuerySet:
        #     print(obj.id,obj.name,obj.password,obj.age)

        # row_obj = UserInfo.objects.filter(age=29).first()  #获取到第一个对象
        # print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)


        # ### 4.更新数据 ###
        # UserInfo.objects.all().update(password=999)
        # UserInfo.objects.filter(age=19).update(password=666)

        return HttpResponse("OK")


# 用户管理
def info_list(request):

    # 获取所有用户信息
    data_list = UserInfo.objects.all()

    # 渲染 返回给用户
    return render(request, 'info_list.html',{"data_list":data_list})
def info_add(request):


    if request.method == 'GET':
        return render(request,"info_add.html")
    if request.method == 'POST':
        # 获取用户提交数据
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")
        print(user,pwd,age)

        # 添加到数据库
        UserInfo.objects.create(name=user,password=pwd,age=age)

        # return HttpResponse("添加成功")
        return redirect("/info/list/")
    return HttpResponse("Error")


def info_delete(request):
    nid  = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")