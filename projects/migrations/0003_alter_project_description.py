# Generated by Django 5.0 on 2023-12-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]