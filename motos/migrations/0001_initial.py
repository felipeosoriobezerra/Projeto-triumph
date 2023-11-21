# Generated by Django 4.2.7 on 2023-11-21 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ano', models.IntegerField()),
                ('imagem_1', models.ImageField(blank=True, null=True, upload_to='motos/')),
                ('imagem_2', models.ImageField(blank=True, null=True, upload_to='motos/')),
                ('imagem_3', models.ImageField(blank=True, null=True, upload_to='motos/')),
                ('imagem_4', models.ImageField(blank=True, null=True, upload_to='motos/')),
                ('imagem_5', models.ImageField(blank=True, null=True, upload_to='motos/')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motos.marca')),
            ],
        ),
    ]
