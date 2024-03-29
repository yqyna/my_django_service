# Generated by Django 2.2.3 on 2023-01-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWebAccountManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新时间')),
                ('user_id', models.IntegerField(default=0, help_text='用户ID', verbose_name='用户ID')),
                ('web_name', models.CharField(blank=True, help_text='网址名称', max_length=255, null=True, verbose_name='网址名称')),
                ('web_site', models.CharField(blank=True, help_text='网址', max_length=255, null=True, verbose_name='网址')),
                ('account', models.CharField(default='', help_text='注册账号', max_length=150, verbose_name='注册账号')),
                ('password', models.CharField(default='', help_text='账号密码', max_length=128, verbose_name='账号密码')),
                ('mobile', models.CharField(blank=True, help_text='绑定手机号', max_length=255, null=True, verbose_name='绑定手机号')),
                ('email', models.EmailField(blank=True, help_text='绑定邮箱', max_length=255, null=True, verbose_name='绑定邮箱')),
            ],
            options={
                'verbose_name': '用户品台账号管理表',
                'verbose_name_plural': '用户品台账号管理表',
                'db_table': 'app_user_web_account_manage',
                'ordering': ('-create_time',),
            },
        ),
    ]
