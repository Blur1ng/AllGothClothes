# Generated by Django 5.0.7 on 2024-07-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0012_alter_brand_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='type_of_clothing',
            field=models.CharField(max_length=255, verbose_name='Type of clothing'),
        ),
    ]
