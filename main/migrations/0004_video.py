# Generated by Django 3.1.4 on 2021-12-08 14:45

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211208_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
        ),
    ]
