# Generated by Django 3.1.7 on 2021-05-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_conclusion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='code',
        ),
        migrations.RemoveField(
            model_name='post',
            name='conclusion',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media'),
        ),
    ]
