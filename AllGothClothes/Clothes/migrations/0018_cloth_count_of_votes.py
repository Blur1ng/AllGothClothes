# Generated by Django 4.2.16 on 2024-10-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0017_alter_cloth_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='count_of_votes',
            field=models.IntegerField(default=0, verbose_name='Count of votes'),
        ),
    ]
