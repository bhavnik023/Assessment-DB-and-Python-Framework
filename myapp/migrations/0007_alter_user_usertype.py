# Generated by Django 4.2.7 on 2024-01-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='patients', max_length=100),
        ),
    ]