# Generated by Django 4.0.1 on 2022-03-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_category_pid_products_catid'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pImage',
            field=models.ImageField(default=0, upload_to='pics/'),
        ),
    ]
