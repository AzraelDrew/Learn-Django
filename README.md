# Learn-Django

#### Django3 学习记录

> 安装 Django

```shell
pip3 install django==version
```

> 创建项目

```shell
django-admin startproject projectname
```

> 默认文件介绍

```shell
mysite
├── manage.py       //项目管理、启动项目、创建app、数据管理(---经常使用---)
└── mysite
    ├── __init__.py
    ├── asgi.py     //接收网络请求(不需要改)
    ├── settings.py //项目配置(---经常修改---)
    ├── urls.py     //url和函数的对应关系(---经常修改---)
    └── wsgi.py     //接收网络请求(不需要改)
```

> App

```
- 项目
    - app，用户管理
    - app，网站
    - app API
    //每个app互不影响
    //一般一个项目就创建一个app
```

> 创建 App

````shell
python3 manage.py startapp appname
```http://127.0.0.1:8000/upload/form/

> App 项目结构

````

app
├── **init**.py
├── admin.py //固定不用动,Django 默认提供的 admin 后台管理
├── apps.py //固定不用动,app 启动类
├── migrations //固定不用动,数据库变更记录
│ └── **init**.py
├── models.py //对数据库进行操作(重要)
├── tests.py //固定不用动,单元测试
└── views.py //函数(重要)

````

> 启动运行 App

注册 app 在 setting.py 中的 INSTALLED_APPS 中添加 appname.apps.AppConfig [setting.py]

![](./img/alex01.png)

编写 URL 和视图函数的对应关系 [urls.py]

![](./img/alex05.png)

编写视图函数 [views.py]

![](./img/alex02.png)

启动 Django 项目

```shell
python3 manage.py runserver   然后访问http://127.0.0.1:8000/index
````

> URL 与函数的对应关系

```
url->函数->执行函数
```

![](./img/alex03.png)

> templates 模版

![](./img/alex04.png)

> 静态文件

**开发过程中一般将**:

- 图片
- css
- js

**都视为静态文件存放在/appname/static/下**

![](./img/alex.png)

> 引用静态文件

![](./img/alex06.png)

> 模版语法

_本质上:在 HTML 中写一些占位符,由数据对这些占位符进行替换和处理_

![](./img/template_syntax.png)

> 请求和响应

![](./img/alex08.png)

redirect 重定向工作方式如下(Django 返回一个值后,浏览器再去向这个页面发起请求)

![](./img/alex07.png)

> form 表单提交报错

![](./img/alex09.png)

解决办法(在 form 表单内部添加 {% csrf_token %} )

![](./img/alex10.png)

> Django 使用 ORM 操作数据库

![](./img/alex11.png)

安装第三方模块

```shell
pip3 install mysqlclient
```

> ORM

创建、修改、删除数据库中的表(不用写 SQL 语句);[无法创建数据库] 操作表中的数据(不用写 SQL 语句)

> Django 连接数据库

在 setting.py 中进行配置和修改

> Django 操作表(在 models.py 中)

- 创建表

```python
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


"""

上述代码等同于
create table appname_classname[小写的类名](
    id bigint auto_increment primary key,   此行为自动生成
    name varchar(32),
    password varchar(64),
    age int
)

"""


# 在此之前app必须注册
# setting.py  INSTALLED_APPS中添加      'app.apps.AppConfig'  #appname下apps.py中的AppnameConfig(第一个class)


python3 manage.py makemigrations  # 检查是否更改

python3 manage.py migrate         # 应用更改
```

- 删除表

_删除相应的 class 再执行上述命令_

- 修改表

在表中新增列时,由于已存在的的列中可能已有数据，所以新增的列必须要指定数据

- 手动添加

![](./img/alex12.png)

- 允许为空

```python
# 设置默认值
size = models.IntegerField(default=5)
# 允许为空
data = models.IntegerField(null=True,blank=True)
```

> Django 操作表中的数据

![](./img/alex13.png)

> URL 传值

- 匹配

```python
   /depart/<int:nid>/edit/
```

- ?

```python
   /depart/edit/?nid=int&name=str
\0	 `	`
```

> 模版继承

```django
 # 模版
 {% block css %}     {% endblock %}

 <div>
   {% block TagName %}{% endblock %}    # 相当于占位符
 </div>

 {% block js %}      {% endblock %}

```

```django
 # 继承模版

 {% extends "template.html" %}     #必须先继承

 {% block css  %}
     <link
       rel="stylesheet"
       href="{% static 'plugins....min.css'  %}"
     />
 <style>
 	....
 </style>
 {% endblock %}

 {% block TagName %}
 <h1>首页</h1>         # 替换占位符
 {% endblock %}


 {% block js %}
 <script src="{% static 'plugins....min.js'  %}"></script>
 <script>
 	...
 </script>
 {% endblock %}
```

![](./img/alex14.png)

![](./img/alex15.png)

![](./img/alex16.png)

![](./img/alex17.png)

![](./img/alex18.png)

> FORM 组件

views.py

```python
class MyForm(Form):
  	# 创建表单需要渲染或者提交的数据
    #  widget   #扩展
    user = forms.CharField(widget=forms.Input)
    pwd = form.CharFiled(widget=forms.Input)
    email = form.CharFiled(widget=forms.Input)
    account = form.CharFiled(widget=forms.Input)
    create_time = form.CharFiled(widget=forms.Input)
    depart = form.CharFiled(widget=forms.Input)
    gender = form.CharFiled(widget=forms.Input)


def user_add(request):
    if request.method == "GET":
      	# 示例化Form
        form = MyForm()
        return render(request, 'template.html',{"form":form})
```

template.html

```django

手动渲染
<form method="post">
    {{ form.user }}
    {{ form.pwd }}
    {{ form.email }}
    <!-- <input type="text"  placeholder="姓名" name="user" /> -->
</form>


循环渲染

<form method="post">
    {% for field in form%}
    	{{ field }}
    {% endfor %}
    <!-- <input type="text"  placeholder="姓名" name="user" /> -->
</form>
```

> ModelForm 组件(针对数据库中的某个表)

models.py

```python
class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
```

views.py

```python
class MyModelForm(ModelForm):
  	# 自定义字段
    xx = form.CharField*("...")
    class Meta:
        model = UserInfo
        # 需要渲染的字段   可以是数据库或者自定义的
        fields = ["name","password","age","xx"]


def api (request):
    if request.method == "GET":
        form = MyForm()
        return render(request, 'template.html',{"form":form})
```

template.html

```django

手动渲染
<form method="post">
    {{ form.user }}
    {{ form.pwd }}
    {{ form.email }}
    <!-- <input type="text"  placeholder="姓名" name="user" /> -->
</form>


循环渲染

<form method="post">
    {% for field in form%}
    	{{ field }}
    {% endfor %}
    <!-- <input type="text"  placeholder="姓名" name="user" /> -->
</form>
```

ModeForm 定义插件

```python

class MyModelForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age"]
```

批量定义插件

```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
				field.widget.attrs["class"] = "form-control"
				field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }
```

自定义类

```python
class BootStrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
				field.widget.attrs["class"] = "form-control"
				field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }
```

继承使用

```python
class UserEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age",]
```

> Cookie 与 Session

- cookie:随机字符串
- session:用户信息

```python
# 设置session
request.session["info"] = {"id":object.id,"name":object.name}

# 获取session
info = reuqest.session.get("info")
```

> 使用 cookie 与 session 实现免密码登录

```python
# 登录时生成cookie与session
def login(request):
  ...
  request.session["info"] = {"id":object.id,"name":object.name}
  ...

# 验证是否已经登录
# 在视图函数前统一加入判断
info = request.session.get("info")
if not info:
  return redirect("/login/")
...
```

> 中间件实现验证是否登录

- 定义中间件

```python
from django.utils.deprecation import MiddlewareMixin
# 定义中间件
class M1(MiddlewareMixin):
    """ 中间件1 """
		# 请求时触发的函数  (函数名不能改)
    # 如果方法中没有返回值（返回None），继续向后走
		# 如果有返回值 HttpResponse、render 、redirect，则不再继续向后执行。
    def process_request(self, request):

        # 如果方法中没有返回值（返回None），继续向后走
        # 如果有返回值 HttpResponse、render 、redirect
        print("M1.process_request")
        return HttpResponse("无权访问")
		# 响应时触发的函数  (函数名不能改)
    def process_response(self, request, response):
        print("M1.process_response")
        return response

# 实现登录校验

class AuthLoginMiddleware(MiddlewareMixin):
  def process_request(self, request):
        # 排除那些不需要登录就能访问的页面
        # request.path_info 获取当前用户请求的URL /login/
        if request.path_info == "/login/":
            return

        # 读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走。
        info_dict = request.session.get("info")
        print(info_dict)
        if info_dict:
            return

        # 2.没有登录过，重新回到登录页面
        return redirect('/login/')
```

- 注册中间件

```python
MIDDLEWARE = [
    'appname.middleware.auth.AuthMiddleware',
]
```

> Ajax 请求

- Django

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt   # 免除csrf_token认证
def task_ajax(request):
    data_dict = {"status": True, 'data': [11, 22, 33, 44]}
    # 返回JSON数据 (方式一)
    return HttpResponse(json.dumps(data_dict))
  	# 返回JSON数据 (方式二)
    return JsonResponse(data_dict)
```

- JavaScript

```JavaScript
$(function () {
            // 页面框架加载完成之后代码自动执行
            bindBtnEvent();

        })

        function bindBtnEvent() {
            $("#btn1").click(function () {
                $.ajax({
                    url: '/task/ajax/', // 请求的api
                    type: "post",       // 请求类型
                    data: {             // 请求数据
                        n1: 123,
                        n2: 456
                    },
                    dataType: "JSON",   // 设置返回的数据类型 (自动序列化)
                    success: function (res) {
                        console.log(res);
                    }
                })
            })
        }
```
