# Generated by Django 4.2.7 on 2023-11-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0009_alter_moto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
