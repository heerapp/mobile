# Generated by Django 3.1.4 on 2021-12-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211208_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
