# Generated by Django 2.2.3 on 2023-02-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_systemcommonconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemcommonconfig',
            name='access_token',
            field=models.CharField(blank=True, help_text='授权token', max_length=255, null=True, verbose_name='授权token'),
        ),
    ]
