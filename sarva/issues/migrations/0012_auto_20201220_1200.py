# Generated by Django 2.2.2 on 2020-12-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_auto_20201220_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='pic1',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='pic2',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='pic3',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='propic',
            field=models.CharField(max_length=600),
        ),
    ]
