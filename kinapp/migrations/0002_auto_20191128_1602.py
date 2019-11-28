# Generated by Django 2.2.7 on 2019-11-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('hotel', models.CharField(blank=True, max_length=50)),
                ('checkin', models.DateField(auto_now=True)),
                ('checkout', models.DateField()),
                ('amount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='bookings',
        ),
    ]