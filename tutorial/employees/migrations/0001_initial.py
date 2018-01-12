# Generated by Django 2.0.1 on 2018-01-10 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phoneno', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'", regex='^\\+?[0-9]+?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=120, null=True, unique=True)),
                ('role', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
