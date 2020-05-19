# Generated by Django 3.0.5 on 2020-05-19 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0005_auto_20200519_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('instore', 'In Store'), ('inuse', 'In Use'), ('discontinued', 'Discontinued')], default='instore', max_length=30)),
                ('purchaseDate', models.DateField(blank=True, null=True, verbose_name='Purchase Date')),
                ('purchaseCost', models.IntegerField(blank=True, null=True, verbose_name='Purchase Cost')),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.Asset')),
                ('purchaseOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.PurchaseOrder', verbose_name='Linked Purchase Order')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maintenance.Site')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.Supplier')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
