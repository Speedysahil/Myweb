# Generated by Django 3.2.7 on 2021-10-29 13:25

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orderupdate'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='orders',
            managers=[
                ('product', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='orderupdate',
            managers=[
                ('product', django.db.models.manager.Manager()),
            ],
        ),
    ]
