# Generated by Django 2.2.2 on 2020-12-20 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0015_complaints_chats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='chats',
        ),
    ]
