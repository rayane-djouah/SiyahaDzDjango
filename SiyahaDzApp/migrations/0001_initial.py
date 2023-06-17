# Generated by Django 4.2.1 on 2023-06-17 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentralEmployee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='centralemployee', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('theme', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('views_count', models.IntegerField(default=0)),
                ('openhour', models.TimeField(default=None)),
                ('closehour', models.TimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='RegionalEmployee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='regionalemployee', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='tourist', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to='storage/point_of_interest/videos')),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.pointofinterest')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfInterest_Transportation',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.pointofinterest')),
                ('transportation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.transportation')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='storage/point_of_interest/photos')),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.pointofinterest')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('opendate', models.DateField()),
                ('closedate', models.DateField()),
                ('image', models.ImageField(upload_to='storage/photoevent/')),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.pointofinterest')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.pointofinterest')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiyahaDzApp.tourist')),
            ],
        ),
    ]
