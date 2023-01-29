# 使用中间件进行鉴权

from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import HttpResponse,redirect

class AuthLoginMiddleware(MiddlewareMixin):
    def process_request(self,request):    # 函数名不能改
        # 在process_request中:
        # 若没有返回值  则默认返回none   继续向后走
        # 若有返回值  则直接从当前中间件开始向前一个中间件或浏览器返回
        # print("enter middleware")

        # 忽略不需要登录就能访问的页面
        # request.path_info   获取当前用户请求都url   /login/

        # print(request.path_info)

        if request.path_info in ["/login/","/image/code/","/task/ajax/"]:
            return

        # 获取当前用户都seeion信息   如果有则代表已经登录  则继续向后走
        info_dict  =  request.session.get("info")
        # print("middleware",info_dict)
        if  info_dict:
            return 
        # 若没有登录,返回登录页面
        return redirect("/login/")

    # def process_response(self,request,response):   # 函数名不能改
    #     print("exit middleware")
    #     return response