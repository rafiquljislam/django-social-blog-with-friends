# Generated by Django 3.0.8 on 2020-07-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='image/profile.png', null=True, upload_to='image/'),
        ),
    ]