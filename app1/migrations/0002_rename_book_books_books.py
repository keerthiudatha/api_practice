# Generated by Django 5.0.1 on 2024-01-25 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='book',
            new_name='books',
        ),
    ]
