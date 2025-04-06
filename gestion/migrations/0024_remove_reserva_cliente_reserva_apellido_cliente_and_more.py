# Generated by Django 4.2 on 2024-10-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0023_alter_reserva_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='cliente',
        ),
        migrations.AddField(
            model_name='reserva',
            name='apellido_cliente',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='cedula_cliente',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombre_cliente',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
