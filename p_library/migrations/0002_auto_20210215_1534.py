# Generated by Django 2.2.6 on 2021-02-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publishing_house',
            new_name='Publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, upload_to='books_photo'),
        ),
    ]
