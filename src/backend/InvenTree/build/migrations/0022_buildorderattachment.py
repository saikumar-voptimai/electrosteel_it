# Generated by Django 3.0.7 on 2020-10-26 04:17

import InvenTree.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('build', '0021_auto_20201020_0908_squashed_0026_auto_20201023_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildOrderAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(help_text='Select file to attach', upload_to='attachments')),
                ('comment', models.CharField(blank=True, help_text='File comment', max_length=100)),
                ('upload_date', models.DateField(auto_now_add=True, null=True)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='build.Build')),
                ('user', models.ForeignKey(blank=True, help_text='User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
