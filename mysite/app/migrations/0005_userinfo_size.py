# Generated by Django 4.1.3 on 2022-12-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='size',
            field=models.IntegerField(default=2),
        ),
    ]
