# Generated by Django 4.0.6 on 2022-10-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_playerrank_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerrank',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
