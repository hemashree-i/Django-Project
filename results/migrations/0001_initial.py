# Generated by Django 4.1.4 on 2023-01-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('standard', models.IntegerField()),
                ('marks1', models.IntegerField()),
                ('marks2', models.IntegerField()),
                ('marks3', models.IntegerField()),
                ('marks4', models.IntegerField()),
            ],
        ),
    ]
