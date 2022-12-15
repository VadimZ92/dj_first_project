# Generated by Django 4.1.2 on 2022-11-15 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Measurements', to='measurement.sensor')),
            ],
        ),
    ]