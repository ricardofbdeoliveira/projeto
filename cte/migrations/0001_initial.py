# Generated by Django 3.0.3 on 2020-02-03 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cte', models.IntegerField()),
                ('cliente', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('emissao', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=8)),
                ('frete', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
