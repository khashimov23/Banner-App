# Generated by Django 3.2.6 on 2021-09-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_remove_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]