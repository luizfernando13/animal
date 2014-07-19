# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r

class SubscribeTest(TestCase):
def setUp(self):
self.resp = self.client.get('/inscricao/')
#self.resp = self.client.get(r('subscriptions:subscribe')) ref

def test_get(self):
'GET /inscricao/ must return status code 200.'
self.assertEqual(200, self.resp.status_code)

class SubscribePostTest(TestCase):
def setUp(self):
data = dict(name='Henrique Bastos', cpf='12345678901',
email='henrique@bastos.net', phone='21-96186180')
self.resp = self.client.post('/inscricao/', data)
#self.resp = self.client.post(r('subscriptions:subscribe'), data) ref
def test_post(self):
'Valid POST should redirect to /inscricao/1/'
self.assertEqual(302, self.resp.status_code)
def test_save(self):
'Valid POST must be saved.'
self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
def setUp(self):
data = dict(name='Henrique Bastos', cpf='000000000012',
email='henrique@bastos.net', phone='21-96186180')
self.resp = self.client.post('/inscricao/', data)
#self.resp = self.client.post(r('subscriptions:subscribe'), data) ref
def test_post(self):
'Invalid POST should not redirect.'
self.assertEqual(200, self.resp.status_code)
def test_form_errors(self):
'Form must contain errors.'
self.assertTrue(self.resp.context['form'].errors)
def test_dont_save(self):
'Do not save data.'
self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
def test_template_has_non_field_errors(self):
'Check if non_field_errors are shown in template.'
invalid_data = dict(name='Henrique Bastos', cpf='12345678901')
response = self.client.post(r('subscriptions:subscribe'), invalid_data)
self.assertContains(response, '<ul class="errorlist">')#{{ form.non_field_errors }}