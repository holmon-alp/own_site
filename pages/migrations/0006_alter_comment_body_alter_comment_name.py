# Generated by Django 4.0.5 on 2022-08-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(default='Izoh', max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='ism', max_length=80),
        ),
    ]