# Generated by Django 4.2 on 2024-10-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_featuremodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuremodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='feature/'),
        ),
    ]
