# Generated by Django 4.1.3 on 2023-01-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('img', models.CharField(max_length=128, verbose_name='头像')),
            ],
        ),
    ]