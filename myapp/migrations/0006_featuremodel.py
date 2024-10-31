# Generated by Django 4.2 on 2024-10-31 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_expmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='feature/')),
            ],
        ),
    ]
