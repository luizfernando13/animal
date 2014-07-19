# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
class DetailTest(TestCase):
def setUp(self):
s = Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
email='henrique@bastos.net', phone='21-96186180')
self.resp = self.client.get('/inscricao/%d/' % s.pk)
#self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))ref
def test_get(self):
'GET /inscricao/1/ should return status 200.'
self.assertEqual(200, self.resp.status_code)
def test_context(self):
'Context must have a subscription instance.'
subscription = self.resp.context['subscription']
self.assertIsInstance(subscription, Subscription)



class DetailNotFound(TestCase):
def test_not_found(self):
response = self.client.get('/inscricao/0/')
#response = self.client.get(r('subscriptions:detail', args=[0])) ref
self.assertEqual(404, response.status_code)

# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
class SpeakerDetailTest(TestCase):
def setUp(self):
url = r('core:speaker_detail', kwargs={'slug': 'henrique-bastos'})
self.resp = self.client.get(url)
def test_get(self):
'GET should result in 200.'
self.assertEqual(200, self.resp.status_code)
def test_template(self):
'Template should be core/speaker_detail.html'
self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')
def test_html(self):
'Html must contain data.'
self.assertContains(self.resp, 'Henrique Bastos')
self.assertContains(self.resp, 'Passionate software developer!')
self.assertContains(self.resp, 'http://henriquebastos.net')

def test_context(self):
'Speaker must be in context.'
speaker = self.resp.context['speaker']
self.assertIsInstance(speaker, Speaker)