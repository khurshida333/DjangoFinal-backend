# Generated by Django 5.0.6 on 2024-10-05 16:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Department', max_length=30)),
                ('slug', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='not provided')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='teacher.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Course', max_length=100)),
                ('description', models.TextField(default='No description provided')),
                ('duration', models.CharField(default='N/A', max_length=100)),
                ('format', models.CharField(default='online', max_length=50)),
                ('key_features', models.TextField(default='No key features provided')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='teacher.teacher')),
            ],
        ),
    ]
