# Generated by Django 4.1.5 on 2023-01-14 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_project_project_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
