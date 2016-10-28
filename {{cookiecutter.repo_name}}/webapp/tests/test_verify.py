# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test import Client
from django.test import TestCase


class VerifyTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.mobile = '18500215943'

    def test_send_verify(self):
        """Animals that can speak are correctly identified"""

        response = self.client.post('/account/verify/', {'openid': 'john', 'mobile': self.mobile})
        response = json.loads(response.content)

        self.assertEqual(response.get('status'), '0')

    # def test_check_verify(self):
    #     """Animals that can speak are correctly identified"""
    #     verify = raw_input(u'verify:')
    #     response = self.client.post('/account/verify/', {'openid': 'john', 'mobile': self.mobile, 'verify': verify})
    #     response = json.loads(response.content)
    #
    #     self.assertEqual(response.get('status'), '0')
