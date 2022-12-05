from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):   #request为默认参数
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

def news(req):
    #在网络上获取数据
    #向  http://www.chinaunicom.com/api/article/NewsByIndex/2/2021/12/news 发送请求
    #利用第三方模块:requests
    import requests
    url = "http://www.chinaunicom.com/api/article/NewsByIndex/2/2022/11/news"
    res=requests.get(url,headers={"User-Agent": "XY"})
    data_list = res.json()
    print(res)
    print(data_list)


    return render(req,'news.html')