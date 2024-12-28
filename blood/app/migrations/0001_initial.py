# Generated by Django 5.1.3 on 2024-12-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('blood_group', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
