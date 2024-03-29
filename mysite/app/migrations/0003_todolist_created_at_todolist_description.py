# Generated by Django 4.2.4 on 2023-09-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default="1900-01-01"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
