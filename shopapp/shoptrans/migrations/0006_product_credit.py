# Generated by Django 2.0.3 on 2018-07-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptrans', '0005_auto_20180721_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='credit',
            field=models.BooleanField(default=False),
        ),
    ]
