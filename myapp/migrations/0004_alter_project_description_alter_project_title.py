# Generated by Django 4.2.6 on 2023-10-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
