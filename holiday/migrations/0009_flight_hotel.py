# Generated by Django 2.0.7 on 2018-08-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0008_holidays_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('to', models.CharField(max_length=20)),
                ('fro', models.CharField(max_length=20)),
                ('depart_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('days', models.CharField(max_length=200)),
                ('airlines', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_day', models.FloatField()),
                ('address', models.TextField()),
                ('category', models.CharField(max_length=5)),
                ('amenities', models.TextField()),
            ],
        ),
    ]