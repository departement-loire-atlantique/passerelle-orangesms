# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_orangesms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orangerestsmsgateway',
            name='default_country_code',
            field=models.CharField(default='33', max_length=3, verbose_name=b'Pr\xc3\xa9fixe pays'),
        ),
        migrations.AlterField(
            model_name='orangerestsmsgateway',
            name='default_trunk_prefix',
            field=models.CharField(default='0', max_length=2, verbose_name=b'Pr\xc3\xa9fixe supprim\xc3\xa9 par d\xc3\xa9faut'),
        ),
        migrations.AlterField(
            model_name='orangerestsmsgateway',
            name='groupname',
            field=models.CharField(max_length=64, verbose_name=b'Groupe'),
        ),
        migrations.AlterField(
            model_name='orangerestsmsgateway',
            name='password',
            field=models.CharField(max_length=64, verbose_name=b'Mot de passe'),
        ),
        migrations.AlterField(
            model_name='orangerestsmsgateway',
            name='username',
            field=models.CharField(max_length=64, verbose_name=b'Identifiant'),
        ),
    ]
