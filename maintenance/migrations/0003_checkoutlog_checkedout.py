# Generated by Django 3.0.5 on 2020-05-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_checkoutlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutlog',
            name='checkedout',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]