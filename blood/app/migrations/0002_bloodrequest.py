# Generated by Django 5.1.4 on 2024-12-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]