# Generated by Django 4.2.7 on 2023-12-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("motos", "0011_alter_moto_preco"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moto",
            name="imagem_1",
            field=models.ImageField(null=True, upload_to="motos/"),
        ),
        migrations.AlterField(
            model_name="moto",
            name="imagem_2",
            field=models.ImageField(null=True, upload_to="motos/"),
        ),
        migrations.AlterField(
            model_name="moto",
            name="imagem_3",
            field=models.ImageField(null=True, upload_to="motos/"),
        ),
        migrations.AlterField(
            model_name="moto",
            name="imagem_4",
            field=models.ImageField(null=True, upload_to="motos/"),
        ),
        migrations.AlterField(
            model_name="moto",
            name="imagem_5",
            field=models.ImageField(null=True, upload_to="motos/"),
        ),
    ]