# Generated by Django 3.1.5 on 2021-02-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20210212_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominee',
            name='description',
            field=models.TextField(max_length=350),
        ),
    ]
