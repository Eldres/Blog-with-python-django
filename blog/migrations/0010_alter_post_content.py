# Generated by Django 4.0.6 on 2022-07-25 15:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
