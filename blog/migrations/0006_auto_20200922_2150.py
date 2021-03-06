# Generated by Django 3.0.3 on 2020-09-22 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200922_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='apporved_comment',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 22, 16, 20, 16, 84694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 22, 16, 20, 16, 83696, tzinfo=utc)),
        ),
    ]
