# Generated by Django 4.2 on 2024-09-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='creado_en',
        ),
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('Activa', 'Activa'), ('Cancelada', 'Cancelada')], default='Activa', max_length=10),
        ),
    ]
