# Generated by Django 4.2.5 on 2023-10-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studyknight', '0003_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='gd',
            name='pub_date',
        ),
    ]
