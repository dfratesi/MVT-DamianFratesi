# Generated by Django 4.0.6 on 2022-07-28 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familia',
            options={'ordering': ['lastname', 'name'], 'verbose_name': 'Familiar', 'verbose_name_plural': 'Familiares'},
        ),
    ]
