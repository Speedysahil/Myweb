# Generated by Django 3.2.7 on 2021-10-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20211002_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]