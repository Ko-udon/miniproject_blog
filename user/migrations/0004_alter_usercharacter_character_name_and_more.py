# Generated by Django 4.2.6 on 2023-11-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_usercharacter_character_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercharacter',
            name='character_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='usercharacter',
            name='profile_word',
            field=models.TextField(blank=True),
        ),
    ]
