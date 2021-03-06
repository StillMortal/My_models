# Generated by Django 3.1.4 on 2020-12-30 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_models", "0005_homeworkresult_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="homeworkresult",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_models.student",
            ),
        ),
        migrations.AddField(
            model_name="homeworkresult",
            name="homework",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_models.homework",
            ),
        ),
    ]
