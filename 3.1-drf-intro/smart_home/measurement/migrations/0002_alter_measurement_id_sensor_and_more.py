# Generated by Django 4.1.2 on 2022-11-19 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='id_sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Measurement', to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
