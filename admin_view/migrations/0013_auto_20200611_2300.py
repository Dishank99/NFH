# Generated by Django 3.0.7 on 2020-06-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0012_auto_20200611_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anniversary',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='events',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='socials',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
    ]