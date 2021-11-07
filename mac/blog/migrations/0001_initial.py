# Generated by Django 3.2.7 on 2021-10-29 13:25

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('head0', models.CharField(max_length=500)),
                ('head1', models.CharField(max_length=500)),
                ('head2', models.CharField(max_length=500)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
            managers=[
                ('title', django.db.models.manager.Manager()),
            ],
        ),
    ]