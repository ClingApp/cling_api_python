# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141028_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorites',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sticker',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscribes',
            name='creation_date',
            field=api.models.UnixTimestampField(null=True, auto_created=True),
            preserve_default=True,
        ),
    ]
