# Generated by Django 3.0.8 on 2020-07-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friend',
            field=models.ManyToManyField(blank=True, to='user.Profile'),
        ),
    ]
