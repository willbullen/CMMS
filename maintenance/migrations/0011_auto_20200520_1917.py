# Generated by Django 3.0.5 on 2020-05-20 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0010_workorder_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='workOrderNumber',
            field=models.CharField(default='1', max_length=100, verbose_name='Work Order Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maintenance.Model', verbose_name='Model/Part Number'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='notes',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Resolution Notes'),
        ),
    ]
