# Generated by Django 4.0.6 on 2022-10-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playerrank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('point', models.IntegerField(max_length=200)),
            ],
        ),
    ]
