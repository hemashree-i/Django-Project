# Generated by Django 4.1.4 on 2023-01-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=20)),
                ('age2', models.IntegerField()),
                ('gender2', models.CharField(max_length=1)),
                ('standard2', models.IntegerField()),
                ('marks12', models.IntegerField()),
                ('marks22', models.IntegerField()),
                ('marks32', models.IntegerField()),
                ('marks42', models.IntegerField()),
            ],
        ),
    ]
