# Generated by Django 3.1 on 2021-07-02 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PasteBin', '0002_auto_20210702_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
