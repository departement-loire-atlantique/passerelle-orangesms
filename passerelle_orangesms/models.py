# -*- coding: utf-8 -*-
from django.db import models

from . import orange_api
from requests import RequestException

from passerelle.utils.jsonresponse import APIError
from passerelle.base.models import SMSResource

class OrangeRestSMSGateway(SMSResource):

    username = models.CharField(verbose_name='Identifiant', max_length=64)
    password = models.CharField(verbose_name='Mot de passe', max_length=64)
    groupname = models.CharField(verbose_name='Groupe', max_length=64)

    default_country_code = models.CharField(verbose_name='Préfixe pays', max_length=3, default=u'33')
    default_trunk_prefix = models.CharField(verbose_name='Préfixe supprimé par défaut', max_length=2, default=u'0')

    manager_view_template_name = 'passerelle/manage/messages_service_view.html'

    class Meta:
        verbose_name = 'Orange REST SMS'
        db_table = 'sms_orangerest'

    def send_msg(self, text, sender, destinations, **kwargs):
        """Send a SMS using the Orange REST"""

        destinations = self.clean_numbers(destinations, self.default_country_code, self.default_trunk_prefix)

        try:
            api = orange_api.OrangeAPI(self.username, self.password)
            api.send(self.groupname, destinations, text)
        except requests.RequestException as e:
            raise APIError('Orange REST SMS API error: %s' % e)

