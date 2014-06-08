from django.db import models
from django.contrib.auth.models import User

class YMHT(models.Model):
  user = models.ForeignKey(User, blank=True, null=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  gnan_date = models.DateField(blank=True, null=True)
  father_name = models.CharField(max_length=255)
  father_contact = models.CharField(max_length=10, blank=True, null=True)
  mother_name = models.CharField(max_length=255)
  mother_contact = models.CharField(max_length=10, blank=True, null=True)

  def __unicode__(self):
    return '%s %s' % (self.first_name, self.last_name)

  class Meta:
    verbose_name_plural = "YMHTians"

class YMHTMobile(models.Model):
  ymht = models.ForeignKey(YMHT)
  mobile = models.CharField(max_length=255)
  is_active = models.BooleanField(default=False)

class YMHTEmail(models.Model):
  ymht = models.ForeignKey(YMHT)
  email = models.EmailField()
  is_active = models.BooleanField(default=False)

class Coordinator(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  user = models.ForeignKey(User, blank=True, null=True)
  date_of_birth = models.DateField()
  gnan_date = models.DateField(blank=True, null=True)

