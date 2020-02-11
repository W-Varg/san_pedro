# Generated by Django 2.1 on 2018-10-03 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjeta', models.CharField(max_length=20)),
                ('date_registry', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('state', models.BooleanField(default=True)),
                ('date_create', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_create'],
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='tarjetas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Tarjeta'),
        ),
    ]