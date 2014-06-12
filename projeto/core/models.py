from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


@models.permalink
def get_absolute_url(self):
return ('core:speaker_detail', (), {'slug': self.slug})

def get_absolute_url(self):
return '/palestras/%d/' % self.pk