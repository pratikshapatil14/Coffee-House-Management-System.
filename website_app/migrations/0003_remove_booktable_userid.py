# Generated by Django 4.2.5 on 2024-02-07 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0002_booktable_phoneno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktable',
            name='userid',
        ),
    ]