# Generated by Django 2.0.4 on 2018-04-19 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0003_auto_20180419_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='date_created',
        ),
    ]
