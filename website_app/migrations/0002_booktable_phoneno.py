# Generated by Django 4.2.5 on 2024-02-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktable',
            name='phoneno',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
