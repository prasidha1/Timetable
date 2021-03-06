# Generated by Django 3.0.5 on 2022-02-06 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 6, 6, 58, 17, 586986, tzinfo=utc), verbose_name='Conversation Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 6, 6, 58, 20, 360196, tzinfo=utc), verbose_name='Conversation Time'),
            preserve_default=False,
        ),
    ]
