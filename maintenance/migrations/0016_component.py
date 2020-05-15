# Generated by Django 3.0.5 on 2020-05-14 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0015_auto_20200513_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100, verbose_name='Tag/Barcode')),
                ('serial', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('notes', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('instore', 'In Store'), ('inuse', 'In Use'), ('onorder', 'On Order'), ('inrepair', 'In Repair'), ('discontinued', 'Discontinued'), ('disposed', 'Disposed')], default='instore', max_length=30)),
                ('purchaseDate', models.DateField(blank=True, null=True, verbose_name='Purchase Date')),
                ('purchaseCost', models.IntegerField(blank=True, null=True, verbose_name='Purchase Cost')),
                ('warrantyExpiration', models.DateField(blank=True, null=True, verbose_name='Warranty Expiration Date')),
                ('manufactureDate', models.DateField(blank=True, null=True, verbose_name='Manufacture Date')),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.Asset')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maintenance.Category')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.Department')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maintenance.Model')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='maintenance.Site')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.Supplier')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='maintenance.OrganizationUsers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
