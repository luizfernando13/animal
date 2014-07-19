# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-96186180'
            )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Henrique Bastos', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):

    def setUp(self):
    # Create a first entry to force the colision
        Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
            email='henrique@bastos.net', phone='21-96186180')

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Henrique Bastos', cpf='12345678901',
            email='outro@email.com', phone='21-96186180')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Henrique Bastos', cpf='00000000011',
            email='henrique@bastos.net', phone='21-96186180')
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
'Email is not unique anymore'
s = Subscription.objects.create(name='Henrique Bastos', cpf='109876543210',
email='henrique@bastos.net')
self.assertEqual(2, s.pk)

    def test_mark_all(self):
'Mark all as paid.'
fake_request = Mock()
queryset = Subscription.objects.all()
self.model_admin.mark_as_paid(fake_request, queryset)
self.assertEqual(1, Subscription.objects.filter(paid=True).count())



def test_speakers(self):
'Talk has many Speakers and vice-versa.'
self.talk.speakers.create(name='Henrique Bastos',
slug='henrique-bastos',
url='http://henriquebastos.net')
self.assertEqual(1, self.talk.speakers.count())