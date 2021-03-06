# Generated by Django 3.0.7 on 2020-09-14 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_remove_previousstarterplanuser_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegisteredProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('username', models.CharField(max_length=200, verbose_name='Email')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True, verbose_name='Gender')),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobile No.')),
                ('class_type', models.CharField(blank=True, choices=[('O', 'Online'), ('A', 'At Hub')], max_length=20, null=True, verbose_name='Class Type')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Approve')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Batches', verbose_name='Batch')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Plans', verbose_name='Plan')),
            ],
            options={
                'verbose_name': 'User Requests',
            },
        ),
    ]
