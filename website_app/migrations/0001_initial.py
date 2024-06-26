# Generated by Django 4.2.5 on 2024-02-07 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='booktable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people', models.IntegerField()),
                ('message', models.CharField(max_length=1000)),
                ('status', models.CharField(default='request submited', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('cdetails', models.CharField(max_length=1000)),
                ('cat', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('cimage', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_id', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=1)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, to='website_app.coffee')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, to='website_app.coffee')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
