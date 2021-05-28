# Generated by Django 3.2.3 on 2021-05-22 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='logo/')),
            ],
            options={
                'verbose_name_plural': 'Logo',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Sektor Tabel',
            },
        ),
        migrations.CreateModel(
            name='StartUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_startup', models.CharField(max_length=200)),
                ('profit', models.CharField(max_length=20)),
                ('image', models.ManyToManyField(to='api.LogoImage')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sector')),
            ],
            options={
                'verbose_name_plural': 'Startup',
            },
        ),
    ]
