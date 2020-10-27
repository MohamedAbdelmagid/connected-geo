# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class BaeaNests(models.Model):
    gid = models.AutoField(primary_key=True)
    postgis_fi = models.BigIntegerField(blank=True, null=True)
    lat_y_dd = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    long_x_dd = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    nest_id = models.BigIntegerField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baea_nests'

    def __str__(self):
        return f'Id: {self.gid}, Nest: {self.nest_id}'


class BaeaSurveys(models.Model):
    id = models.IntegerField(primary_key=True)
    nest = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baea_surveys'

    def __str__(self):
        return f'Id: {self.id}, Nest: {self.nest}'


class BuowlHabitat(models.Model):
    gid = models.AutoField(primary_key=True)
    postgis_fi = models.BigIntegerField(blank=True, null=True)
    habitat = models.CharField(max_length=254, blank=True, null=True)
    hist_occup = models.CharField(max_length=254, blank=True, null=True)
    recentstat = models.CharField(max_length=254, blank=True, null=True)
    habitat_id = models.BigIntegerField(blank=True, null=True)
    active2017 = models.CharField(max_length=10, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buowl_habitat'

    def __str__(self):
        return f'Id: {self.gid}'


class BuowlSurveys(models.Model):
    id = models.IntegerField(primary_key=True)
    habitat = models.IntegerField(blank=True, null=True)
    surveyor = models.CharField(max_length=25, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buowl_surveys'


class GbhRookeries(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    postgis_fi = models.BigIntegerField(blank=True, null=True)
    species = models.CharField(max_length=254, blank=True, null=True)
    activity = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gbh_rookeries'

    def __str__(self):
        return f'{self.id}'


class LinearProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiLineStringField(blank=True, null=True)
    postgis_fi = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    row_width = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    project = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linear_projects'

    def __str__(self):
        return f'Id: {self.id}, Project: {self.project}'


class RaptorNests(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    postgis_fi = models.BigIntegerField(blank=True, null=True)
    lat_y_dd = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    long_x_dd = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    lastsurvey = models.DateField(blank=True, null=True)
    recentspec = models.CharField(max_length=254, blank=True, null=True)
    recentstat = models.CharField(max_length=254, blank=True, null=True)
    nest_id = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raptor_nests'

    def __str__(self):
        return f'Id: {self.gid}, Nest: {self.nest_id}'


class RaptorSurveys(models.Model):
    id = models.IntegerField(primary_key=True)
    nest = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raptor_surveys'

    def __str__(self):
        return f'Id: {self.gid}, Nest: {self.nest}'
