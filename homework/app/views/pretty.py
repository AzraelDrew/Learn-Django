from django.shortcuts import render,redirect           
from django.core.validators import RegexValidator                       # 正则验证
from django.core.exceptions import ValidationError                      # 规则验证报错  
from app import models                                                  # 数据库  
from app.utils.pagination import Pagination                             # 分页组件(实现)
from app.utils.form import PrettyEditModelForm,PrettyModelForm         # BootStrap   ModelForm  样式

# 靓号列表

def pretty_list(request):

    # for i in range(300):
    #     models.PrettyNumber.objects.create(mobile = "18188888888",price=88,level=2,status=2)
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


def pretty_delete(request,nid):
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")