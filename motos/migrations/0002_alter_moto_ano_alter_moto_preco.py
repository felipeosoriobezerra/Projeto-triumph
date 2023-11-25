# Generated by Django 4.2.7 on 2023-11-22 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto',
            name='ano',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='moto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]