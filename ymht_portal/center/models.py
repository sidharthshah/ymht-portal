from django.db import models
from ymht.models import Center, YMHT, Coordinator

def session_content_file_name(instance, filename):
    return '/'.join(['session', instance.user.username, filename])

def session_media_content_file_name(instance, filename):
    return '/'.join(['session_media', instance.user.username, filename])

class Session(models.Model):
  center = models.ForeignKey(Center)
  session_date = models.DateField()
  reported_by = models.ForeignKey(Coordinator)
  session_report = models.TextField()
  comments = models.TextField(blank=True, null=True)
  attachment = models.FileField(upload_to=session_content_file_name, blank=True, null=True)

  def __unicode__(self):
    return 'Session held on %s at %s reported by %s' % (self.session_date, self.center, self.reported_by)

class SessionMedia(models.Model):
  session = models.ForeignKey(Session)
  title = models.CharField(max_length=100, blank=True, null=True)

  CATEGORY_CHOICES = ((1, 'Photo'),
                      (2, 'Video'),
                      (3, 'Other'))

  category = models.IntegerField(choices=CATEGORY_CHOICES)
  attachment = models.FileField(upload_to=session_media_content_file_name, blank=True, null=True)

class Attendance(models.Model):
  session = models.ForeignKey(Session)
  ymht = models.ForeignKey(YMHT)

