# 分页

from django.utils.safestring import mark_safe


""" 
使用分页组件时需要做以下几步:
在视图函数中:

1.获取对应的数据
queryset = models.PrettyNumber.objects.filter(*data_dict).order_by("id")
2.实例化分页对象
page_object = Pagination(request,queryset  )
context ={
    "queryset":page_object.page_queryset,  # 分页完都数据
    "page_string":page_object.html()       # 生成页码
}

在HTML中:

    <tbody>
    {% for item in queryset%}
    <tr>
        <th>{{item.id}}</th>
        <td>{{item.mobile}}</td>
        <td>{{item.price}}</td>
        <td>{{item.get_level_display}}</td>
        <td>{{item.get_status_display}}</td>
        <td>
        <a class="btn btn-primary btn-xs" href="/pretty/{{item.id}}/edit/"
            >编辑</a
        >
        <a class="btn btn-danger btn-xs" href="/pretty/{{item.id}}/delete/"
            >删除</a
        >
        </td>
    </tr>
    {% endfor %}
    <ul class="pagination">
        {{page_string}}
    </ul>
 """
class Pagination(object):
    def __init__(self,request,queryset,page_size=10,page_param="page",plus=7 ):
        # request     请求的数据
        # queryser    符合条件的数据(会根据这个数据进行分页)
        # page_size   每页显示多条数据
        # plus        页码间隔
        # page_param  ulr传递的参数  如:/pretty/lsit?page=12
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutablee =True
        self.query_dict = query_dict

        page = request.GET.get(page_param,"1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        total_count = queryset.count()
        total_page_count , div = divmod(total_count,page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.page_param = page_param
        self.plus = plus
    def html(self):
        if self.total_page_count<= 2 * self.plus + 1:
            start_page =1
            end_page = self.total_page_count
         # 数据较多时
        else:
            # 当前小于5页
            if self.page<=self.plus:
                start_page =1
                end_page = 2*self.plus+1
            else:
                # 当前页+5大于总页面
                if (self.page+self.plus)>self.total_page_count:
                    start_page =self.total_page_count-2*self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page-self.plus
                    end_page = self.page+self.plus
        
        #  页码
        page_str_list=[]
        self.query_dict.setlist(self.page_param,[1])

        # 首页
        page_str_list.append("<li><a href='?{}'>首页</a></li>".format(self.query_dict.urlencode()))

        # 上一页
        if self.page>1:
            self.query_dict.setlist(self.page_param,[self.page-1])
            prev = "<li><a href='?{}'>上一页</a></li>".format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param,[1])
            prev = "<li><a href='?{}'>上一页</a></li>".format(self.query_dict.urlencode())
        page_str_list.append(prev)


        for i in range(start_page,end_page+1 ):
            self.query_dict.setlist(self.page_param,[i])
            if i==self.page:
                ele = "<li class='active' ><a href='?{}'>{}</a></li>".format(self.query_dict.urlencode(),i)
            else:
                 ele = "<li><a href='?{}'>{}</a></li>".format(self.query_dict.urlencode(),i)

            page_str_list.append(ele)


        # 下一页
        if self.page<self.total_page_count:
            self.query_dict.setlist(self.page_param,[self.page+1])
            next = "<li><a href='?{}'>下一页</a></li>".format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param,[self.total_page_count])
            next = "<li><a href='?{}'>下 一页</a></li>".format(self.query_dict.urlencode())
        page_str_list.append(next)

        # 尾页
        self.query_dict.setlist(self.page_param,[self.total_page_count])
        page_str_list.append("<li><a href='?{}'>尾页</a></li>".format(self.query_dict.urlencode()))

        search_string = """    <li>  
        <form method="GET" >
        <div class="input-group">
            <input type="text" name="page" class="form-control" placeholder="页码" style="border-radius: 0;"/>
            <span class="input-group-btn">
            <button class="btn btn-default" type="submit" style="border-radius: 0;">
            跳转</button>
            </button>
            </span> 
        </div>
        </form>
    </li>"""
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string