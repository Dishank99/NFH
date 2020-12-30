# Generated by Django 3.0.7 on 2020-07-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0016_auto_20200612_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='anniversaryimages',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='eventimages',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='socialimages',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='testimonials',
            name='a_img_url',
        ),
        migrations.RemoveField(
            model_name='testimonials',
            name='b_img_url',
        ),
        migrations.AddField(
            model_name='achievements',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/achievements'),
        ),
        migrations.AddField(
            model_name='anniversaryimages',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/misc'),
        ),
        migrations.AddField(
            model_name='eventimages',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/misc'),
        ),
        migrations.AddField(
            model_name='socialimages',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/misc'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='a_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/testimonials', verbose_name='After Image'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='b_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/testimonials', verbose_name='Before Image'),
        ),
    ]
