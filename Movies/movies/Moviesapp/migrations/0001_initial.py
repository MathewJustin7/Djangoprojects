# Generated by Django 4.2.4 on 2023-11-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviesapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.FileField(blank=True, null=True, upload_to='Moviesapp/cover')),
                ('name', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('details', models.CharField(max_length=20)),
            ],
        ),
    ]
