# Generated by Django 4.2.8 on 2023-12-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_articlepost_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=models.TextField(),
        ),
    ]