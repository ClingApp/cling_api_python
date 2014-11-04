#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User as DjangoUser, UserManager
from datetime import datetime
from time import strftime


class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True  # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ = ['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        # Use '%Y%m%d%H%M%S' for MySQL < 4.1
        return strftime('%Y-%m-%d %H:%M:%S', value.timetuple())


# Create your models here.
class UserExtend(DjangoUser):
    """User with app settings."""
    # Use UserManager to get the create_user method, etc.
    # DjangoUser have next fields:
    # username
    # password
    # first_name
    # last_name
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    city = models.CharField(max_length=50, null=True, blank=True)
    objects = UserManager()


class Category(models.Model):
    title = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Review(models.Model):
    user_from = models.ForeignKey(UserExtend, related_name='review_user_from', default=1)
    user_to = models.ForeignKey(UserExtend, related_name='review_user_to', default=1)
    text = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Sticker(models.Model):
    title = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(UserExtend)
    is_deleted = models.BooleanField(default=0)
    categories = models.ManyToManyField(Category)
    creation_date = UnixTimestampField(auto_created=True)


class Comment(models.Model):
    user = models.ForeignKey(UserExtend)
    product = models.ForeignKey(Product)
    text = models.TextField()
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Like(models.Model):
    user = models.ForeignKey(UserExtend)
    product = models.ForeignKey(Product)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Rating(models.Model):
    user_from = models.ForeignKey(UserExtend, null=False, related_name='rating_user_from', default=1)
    user_to = models.ForeignKey(UserExtend, null=False, related_name='rating_user_to', default=1)
    vote = models.BooleanField(default=1)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Favorites(models.Model):
    user = models.ForeignKey(UserExtend)
    product = models.ForeignKey(Product)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)


class Subscribes(models.Model):
    user_from = models.ForeignKey(UserExtend, null=False, related_name='subscribes_user_from', default=1)
    user_to = models.ForeignKey(UserExtend, null=False, related_name='subscribes_user_to', default=1)
    is_deleted = models.BooleanField(default=0)
    creation_date = UnixTimestampField(auto_created=True)
