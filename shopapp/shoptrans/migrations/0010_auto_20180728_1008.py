# Generated by Django 2.0.3 on 2018-07-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptrans', '0009_auto_20180728_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
