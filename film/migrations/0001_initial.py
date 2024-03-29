# Generated by Django 4.1.3 on 2023-03-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('davlat', models.CharField(blank=True, max_length=30)),
                ('tugilgan_yil', models.DateField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('muddat', models.CharField(max_length=30)),
                ('narx', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('janr', models.CharField(max_length=50)),
                ('yil', models.DateField()),
                ('aktyorlar', models.ManyToManyField(to='film.aktyor')),
            ],
        ),
    ]
