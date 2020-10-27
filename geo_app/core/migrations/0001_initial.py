# Generated by Django 3.1.2 on 2020-10-25 16:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaeaNests',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('postgis_fi', models.BigIntegerField(blank=True, null=True)),
                ('lat_y_dd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('long_x_dd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('status', models.CharField(blank=True, max_length=254, null=True)),
                ('nest_id', models.BigIntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'baea_nests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BaeaSurveys',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nest', models.IntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'baea_surveys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuowlHabitat',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('postgis_fi', models.BigIntegerField(blank=True, null=True)),
                ('habitat', models.CharField(blank=True, max_length=254, null=True)),
                ('hist_occup', models.CharField(blank=True, max_length=254, null=True)),
                ('recentstat', models.CharField(blank=True, max_length=254, null=True)),
                ('habitat_id', models.BigIntegerField(blank=True, null=True)),
                ('active2017', models.CharField(blank=True, max_length=10, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'buowl_habitat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuowlSurveys',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('habitat', models.IntegerField(blank=True, null=True)),
                ('surveyor', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'buowl_surveys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GbhRookeries',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('postgis_fi', models.BigIntegerField(blank=True, null=True)),
                ('species', models.CharField(blank=True, max_length=254, null=True)),
                ('activity', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'gbh_rookeries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LinearProjects',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
                ('postgis_fi', models.BigIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=254, null=True)),
                ('row_width', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('project', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'linear_projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RaptorNests',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('postgis_fi', models.BigIntegerField(blank=True, null=True)),
                ('lat_y_dd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('long_x_dd', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('lastsurvey', models.DateField(blank=True, null=True)),
                ('recentspec', models.CharField(blank=True, max_length=254, null=True)),
                ('recentstat', models.CharField(blank=True, max_length=254, null=True)),
                ('nest_id', models.BigIntegerField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'raptor_nests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RaptorSurveys',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nest', models.IntegerField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'raptor_surveys',
                'managed': False,
            },
        ),
    ]