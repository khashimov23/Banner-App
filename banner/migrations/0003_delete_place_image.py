# Generated by Django 3.2.6 on 2021-09-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_alter_place_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place_image',
        ),
    ]