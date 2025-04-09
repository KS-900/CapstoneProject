# Generated by Django 5.1.6 on 2025-04-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='lasst_name',
            new_name='last_name',
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='ShopBE_cust_last_na_c8022c_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='ShopBE_customers',
        ),
    ]
