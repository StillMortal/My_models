# Generated by Django 3.1.4 on 2020-12-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_models', '0003_deadlineerror'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='deadline',
            field=models.DurationField(),
        ),
    ]
