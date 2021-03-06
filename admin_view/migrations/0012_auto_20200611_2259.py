# Generated by Django 3.0.7 on 2020-06-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0011_auto_20200611_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievements',
            options={'verbose_name': 'Achievement', 'verbose_name_plural': 'Achievements'},
        ),
        migrations.AlterModelOptions(
            name='anniversary',
            options={'verbose_name': 'Anniversary', 'verbose_name_plural': 'Anniversaries'},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='notices',
            options={'verbose_name': 'Notice', 'verbose_name_plural': 'Notices'},
        ),
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name': 'Social Cause', 'verbose_name_plural': 'Social Causes'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='desc',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='events',
            name='desc',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='socials',
            name='desc',
            field=models.CharField(max_length=3000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='a_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/testimonials', verbose_name='After Image'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='a_weight',
            field=models.IntegerField(verbose_name='After Weight'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='b_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/testimonials', verbose_name='Before Image'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='b_weight',
            field=models.IntegerField(verbose_name='Before Weight'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='client_name',
            field=models.CharField(max_length=300, verbose_name="Client's Name"),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='duration',
            field=models.CharField(max_length=200, verbose_name='Duration (in months)'),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='review',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name="Client's Review"),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='total_loss',
            field=models.IntegerField(verbose_name='Total Loass (in Kgs)'),
        ),
    ]
