# Generated by Django 2.2.7 on 2019-12-01 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191130_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cover',
            new_name='original_img',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]