# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import passerelle.sms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrangeRestSMSGateway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('slug', models.SlugField(verbose_name='Identifier', unique=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('groupname', models.CharField(max_length=64)),
                ('default_country_code', models.CharField(default='33', max_length=3)),
                ('default_trunk_prefix', models.CharField(default='0', max_length=2)),
                ('users', models.ManyToManyField(to='base.ApiUser', blank=True)),
            ],
            options={
                'db_table': 'sms_orangerest',
                'verbose_name': 'Orange REST SMS',
            },
            bases=(models.Model, passerelle.sms.SMSGatewayMixin),
        ),
    ]
