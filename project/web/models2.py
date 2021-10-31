# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Services(models.Model):
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=15)  # Field name made lowercase.
    phone_number = models.DecimalField(db_column='Phone_Number', unique=True, max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'services'


class Services(models.Model):
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=15)  # Field name made lowercase.
    phone_number = models.DecimalField(db_column='Phone_Number', unique=True, max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'services'
