# Generated by Django 4.2 on 2023-04-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ea3repo', '0007_artifact_quantity_artifact_use_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
