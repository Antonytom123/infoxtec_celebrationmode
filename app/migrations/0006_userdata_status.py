# Generated by Django 4.0.6 on 2022-10-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_enquery_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
