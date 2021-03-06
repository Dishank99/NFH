# Generated by Django 2.1 on 2020-06-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0015_auto_20200612_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='image',
        ),
        migrations.RemoveField(
            model_name='anniversaryimages',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventimages',
            name='image',
        ),
        migrations.RemoveField(
            model_name='socialimages',
            name='image',
        ),
        migrations.RemoveField(
            model_name='testimonials',
            name='a_img',
        ),
        migrations.RemoveField(
            model_name='testimonials',
            name='b_img',
        ),
        migrations.AddField(
            model_name='achievements',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='anniversaryimages',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='eventimages',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='socialimages',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='a_img_url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='b_img_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
