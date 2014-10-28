# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('is_deleted', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.CharField(max_length=500, null=True, blank=True)),
                ('is_deleted', models.BooleanField(default=0)),
                ('categories', models.ManyToManyField(to='api.Category')),
                ('user', models.ForeignKey(to='api.UserExtend')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.BooleanField(default=1)),
                ('is_deleted', models.BooleanField(default=0)),
                ('user_from', models.ForeignKey(related_name=b'rating_user_from', default=1, to='api.UserExtend')),
                ('user_to', models.ForeignKey(related_name=b'rating_user_to', default=1, to='api.UserExtend')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscribes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_deleted', models.BooleanField(default=0)),
                ('user_from', models.ForeignKey(related_name=b'subscribes_user_from', default=1, to='api.UserExtend')),
                ('user_to', models.ForeignKey(related_name=b'subscribes_user_to', default=1, to='api.UserExtend')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(to='api.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to='api.UserExtend'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorites',
            name='product',
            field=models.ForeignKey(to='api.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(to='api.UserExtend'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='api.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='api.UserExtend'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='user_from',
            field=models.ForeignKey(related_name=b'review_user_from', default=1, to='api.UserExtend'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='user_to',
            field=models.ForeignKey(related_name=b'review_user_to', default=1, to='api.UserExtend'),
            preserve_default=True,
        ),
    ]
