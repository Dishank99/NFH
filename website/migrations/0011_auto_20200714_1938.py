# Generated by Django 3.0.7 on 2020-07-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20200714_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='date_time_of_subscription',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
