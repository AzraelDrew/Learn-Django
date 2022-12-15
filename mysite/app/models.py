from django.db import models

# Create your models here.

#固定语法  class user_info(models,Model):
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
    # size = models.IntegerField(default=2)
    # data = models.IntegerField(null=True,blank=True)   #可以为空

"""
上述代码等同于
create table appname_classname[小写的类名](
    id bigint auto_increment primary key,   此行为自动生成
    name varchar(32),
    password varchar(64),
    age int
)
"""
 

# UserInfo.objects.create(name="azrael",password="123",age=18)   #等价于 insert into app_userinfo(name,password,age) values("azrael","123",18)


class Deparment(models.Model):
    title = models.CharField(max_length=16)


# 新建数据
# Deparment.objects.create(title="销售部")  #等价于insert into app_deparment(title) values("销售部")