# Generated by Django 4.0.3 on 2022-04-16 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina1app', '0003_alter_solicitud_adopcion_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto_mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_mascota', models.ImageField(blank=True, upload_to='fotos_mascotas')),
            ],
        ),
        migrations.RemoveField(
            model_name='registro_mascota',
            name='foto_mascota',
        ),
        migrations.AlterField(
            model_name='registro_mascota',
            name='fecha_rescate_mascota',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='registro_mascota',
            name='fecha_vacuna_mascota',
            field=models.DateField(),
        ),
    ]
