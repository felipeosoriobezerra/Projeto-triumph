# Generated by Django 4.2.5 on 2023-09-06 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="stand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.stand"
            ),
        ),
    ]