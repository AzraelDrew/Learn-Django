# Generated by Django 4.1.3 on 2022-12-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_userinfo_data_remove_userinfo_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=2),
        ),
    ]
