# Generated by Django 2.2 on 2023-12-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_articlepost_total_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
