# Generated by Django 3.0.7 on 2020-07-14 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_auto_20200714_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class_type',
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.CharField(blank=True, choices=[('O', 'Online'), ('A', 'At Hub')], max_length=20, null=True)),
                ('batch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Batches')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]