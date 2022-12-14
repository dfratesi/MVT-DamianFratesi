# Generated by Django 4.0.6 on 2022-07-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=20, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('relation', models.CharField(choices=[('Padre', 'Padre'), ('Hermano/a', 'Hermano/a'), ('Madre', 'Madre')], max_length=10, null=True, verbose_name='Relación')),
            ],
        ),
    ]
