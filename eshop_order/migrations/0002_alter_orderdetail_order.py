# Generated by Django 3.2.5 on 2021-08-07 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_order.order', verbose_name='سبد خرید'),
        ),
    ]
