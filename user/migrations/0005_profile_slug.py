# Generated by Django 3.0.8 on 2020-07-02 11:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200702_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='user'),
        ),
    ]
