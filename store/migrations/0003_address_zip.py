# Generated by Django 4.1.1 on 2022-09-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
