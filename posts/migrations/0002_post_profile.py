# Generated by Django 4.1.1 on 2022-09-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
