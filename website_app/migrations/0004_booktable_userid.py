# Generated by Django 4.2.5 on 2024-02-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0003_remove_booktable_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktable',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
