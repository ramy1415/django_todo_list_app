# Generated by Django 3.0.6 on 2020-05-31 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='item',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
