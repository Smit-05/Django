# Generated by Django 4.0.3 on 2022-04-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_catid_products_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]