# Generated by Django 5.1.3 on 2024-12-04 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('M', 'Morning'), ('E', 'Evening')], default='M', max_length=1)),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.fish')),
            ],
        ),
    ]