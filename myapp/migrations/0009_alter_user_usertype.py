# Generated by Django 4.2.7 on 2024-01-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_profile_picture_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='', max_length=100),
        ),
    ]