# Generated by Django 3.0.7 on 2020-07-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200714_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='date_time_of_subscription',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
