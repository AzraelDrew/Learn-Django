

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

```shell
python3 manage.py startapp appname
```

> App 项目结构

```
app
├── __init__.py
├── admin.py          //固定不用动,Django默认提供的admin后台管理
├── apps.py           //固定不用动,app启动类
├── migrations        //固定不用动,数据库变更记录
│   └── __init__.py
├── models.py         //对数据库进行操作(重要)
├── tests.py          //固定不用动,单元测试
└── views.py          //函数(重要)
```

> 启动运行 App

- 注册 app  在setting.py中的  INSTALLED_APPS中添加  appname.apps.AppConfig   [setting.py]

![](/Users/alex/Desktop/Learn-Django/alex01.png)

- 编写 URL 和视图函数的对应关系   [urls.py]

![](/Users/alex/Desktop/Learn-Django/alex05.png)

- 编写视图函数  [views.py]

![](/Users/alex/Desktop/Learn-Django/alex02.png)

- 启动Django项目

  ```shell
  python3 manage.py runserver   然后访问http://127.0.0.1:8000/index
  ```

  

> URL与函数的对应关系

```
url->函数->执行函数
```

![](/Users/alex/Desktop/Learn-Django/alex03.png)

> templates模版

![](/Users/alex/Desktop/Learn-Django/alex04.png)

> 静态文件

**开发过程中一般将**:

- 图片
- css
- js

**都视为静态文件存放在/appname/static/下**

![](/Users/alex/Desktop/Learn-Django/alex.png)

- 引用静态文件

![](/Users/alex/Desktop/Learn-Django/alex06.png)

> 模版语法

*本质上:在HTML中写一些占位符,由数据对这些占位符进行替换和处理*

![](/Users/alex/Desktop/Learn-Django/template_syntax.png)
