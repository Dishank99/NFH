# Generated by Django 3.0.7 on 2020-09-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_preregisteredprofiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_last_active',
            field=models.DateField(blank=True, null=True),
        ),
    ]
