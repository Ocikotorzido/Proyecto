# Generated by Django 3.1.2 on 2020-11-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0009_auto_20201105_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cod_producto',
            field=models.IntegerField(unique=True),
        ),
    ]
