# Generated by Django 4.2.3 on 2023-07-14 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rocket',
            old_name='model',
            new_name='edition',
        ),
    ]
