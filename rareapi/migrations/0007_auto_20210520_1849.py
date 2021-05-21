# Generated by Django 3.2.3 on 2021-05-20 18:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0006_auto_20210519_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 49, 15, 774789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(upload_to='post-images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 49, 15, 778493, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rareuser',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 49, 15, 780478, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='image_url',
            field=models.ImageField(upload_to='reaction_images'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 49, 15, 783013, tzinfo=utc)),
        ),
    ]
