# Generated by Django 4.2.5 on 2023-09-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='Posts'),
            preserve_default=False,
        ),
    ]
