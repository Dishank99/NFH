# Generated by Django 3.0.3 on 2020-05-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0003_auto_20200527_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media/achievements'),
        ),
    ]
