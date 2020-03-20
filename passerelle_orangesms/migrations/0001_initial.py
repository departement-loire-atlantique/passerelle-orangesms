# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_loggingparameters_trace_emails'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrangeRestSMSGateway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(unique=True, verbose_name='Identifier')),
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
            bases=(models.Model,),
        ),
    ]
