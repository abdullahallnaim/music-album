# Generated by Django 4.0 on 2022-03-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_rename_relase_date_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(),
        ),
    ]
