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

class Country(models.Model):
  name = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Countries'

class State(models.Model):
  name = models.CharField(max_length=255)
  country = models.ForeignKey(Country)

  def __unicode__(self):
    return '%s, %s' % (self.name, self.country)


class City(models.Model):
  name = models.CharField(max_length=255)
  state = models.ForeignKey(State)

  def __unicode__(self):
    return '%s, %s' % (self.name, self.state.name)

  class Meta:
    verbose_name_plural = 'Cities'

class YMHTAddress(models.Model):
  ymht = models.ForeignKey(YMHT)
  address_1 = models.CharField(max_length=255)
  address_2 = models.CharField(max_length=255, blank=True, null=True)
  address_3 = models.CharField(max_length=255, blank=True, null=True)
  landmark = models.CharField(max_length=255, blank=True, null=True)
  city = models.ForeignKey(City)
  zipcode = models.CharField(max_length=6)
  is_active = models.BooleanField(default=False)

class Coordinator(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  user = models.ForeignKey(User, blank=True, null=True)
  date_of_birth = models.DateField()
  gnan_date = models.DateField(blank=True, null=True)

class Center(models.Model):
  CATEGORY_CHOICES = ((1, 'BMHT'),
                      (2, 'LMHT'),
                      (3, 'YMHT'))
  category = models.IntegerField(choices=CATEGORY_CHOICES)
  coordinators = models.ManyToManyField(Coordinator)
  established_since = models.DateField()
  locality = models.CharField(max_length=255)
  address_1 = models.CharField(max_length=255)
  address_2 = models.CharField(max_length=255, blank=True, null=True)
  address_3 = models.CharField(max_length=255, blank=True, null=True)
  landmark = models.CharField(max_length=255, blank=True, null=True)
  city = models.ForeignKey(City)
  zipcode = models.CharField(max_length=6)

  def __unicode__(self):
    return '%s, %s' % (self.locality, self.city)

class Membership(models.Model):
  ROLE_CHOICES = ((1, 'Participant'),
                  (2, 'Coordinator'),
                  (3, 'Helper'))

  AGE_GROUP_CHOICES = ((1, '13 to 16'),
                       (2, '17 to 21'),
                       (3, '13 to 21'),
                       (4, '21 to 30'))

  ymht = models.ForeignKey(YMHT)
  coordinator = models.ForeignKey(Coordinator)
  center = models.ForeignKey(Center)
  age_group = models.IntegerField(choices=AGE_GROUP_CHOICES)
  role = models.IntegerField(choices=ROLE_CHOICES)
  since = models.DateField()
  till = models.DateField()

EVENT_CATEGORY_CHOICES = ((0, 'GNC Day'),
                    (1, 'Summer Camp'),
                    (2, 'YUVA Camp'),
                    (3, 'Aptaputra Satsang'),
                    (4, 'General Satsang'),
                    (5, 'Parayan'),
                    (6, 'Janm Jayanti'),
                    (7, 'Picnic'))

class Event(models.Model):


  held_on = models.DateField()
  category = models.IntegerField(choices=EVENT_CATEGORY_CHOICES)
  location = models.ForeignKey(City)

  def __unicode__(self):
    return '%s: %s, %s' % (dict(EVENT_CATEGORY_CHOICES).get(self.category), self.held_on, self.location)

class SevaDetails(models.Model):
  ATTENDED_DETAILS = ((1, 'All Days'), (2, 'Partial Days'))
  event = models.ForeignKey(Event)
  ymht = models.ForeignKey(YMHT)
  coordinator = models.ForeignKey(Coordinator)
  attended = models.IntegerField(choices=ATTENDED_DETAILS)
  attended_days = models.IntegerField(blank=True, null=True)
  comments = models.CharField(max_length=100, blank=True, null=True)

  class Meta:
    verbose_name_plural = 'Seva Details'
