# Generated by Django 3.1.2 on 2020-11-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0010_auto_20201105_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
