# Generated by Django 4.1.5 on 2023-01-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_img',
            field=models.ImageField(blank=True, null=True, upload_to='project-img/'),
        ),
    ]
