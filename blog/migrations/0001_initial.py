# Generated by Django 4.0.6 on 2022-07-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.FileField(upload_to='')),
                ('slug', models.SlugField(allow_unicode=True)),
                ('content', models.TextField()),
                ('excerpt', models.CharField(max_length=150)),
            ],
        ),
    ]
