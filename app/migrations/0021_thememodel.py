# Generated by Django 4.2.7 on 2024-01-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20230131_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=255)),
            ],
        ),
    ]
