# Generated by Django 5.0.7 on 2024-07-31 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0013_alter_cloth_type_of_clothing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='photo',
            field=models.ImageField(upload_to='media/Clothes/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='sold',
            field=models.BooleanField(default=False, verbose_name='Sold?'),
        ),
    ]