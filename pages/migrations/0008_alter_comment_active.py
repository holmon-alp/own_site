# Generated by Django 4.0.5 on 2022-08-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_comment_body_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
