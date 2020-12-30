# Generated by Django 2.1 on 2020-06-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0013_auto_20200611_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='achievements'),
        ),
        migrations.AlterField(
            model_name='anniversaryimages',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='misc'),
        ),
        migrations.AlterField(
            model_name='eventimages',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='misc'),
        ),
        migrations.AlterField(
            model_name='socialimages',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='misc'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='a_img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='testimonials', verbose_name='After Image'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='b_img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='testimonials', verbose_name='Before Image'),
        ),
    ]