# Generated by Django 4.0.3 on 2022-04-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina1app', '0002_remove_registro_mascota_foto_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_mascota',
            name='foto_mascota',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_mascotas'),
        ),
    ]
