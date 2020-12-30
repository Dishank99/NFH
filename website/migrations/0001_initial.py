# Generated by Django 3.0.7 on 2020-07-14 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('timings', models.CharField(max_length=100, verbose_name='Timings')),
                ('for_category', models.CharField(choices=[('U', 'Unisex'), ('F', 'Female')], max_length=50, verbose_name='Category')),
                ('session_link', models.CharField(blank=True, max_length=800, null=True, verbose_name='Session Link')),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_line', models.CharField(max_length=200, verbose_name='Tag Line')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.CharField(max_length=50, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='PlanPerks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Text')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Plans')),
            ],
            options={
                'verbose_name': 'Plan Perk',
                'verbose_name_plural': 'Plan Perks',
            },
        ),
    ]