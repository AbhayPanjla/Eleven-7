# Generated by Django 4.2.5 on 2023-09-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studyknight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_txt', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
