from django.db import models
from ymht.models import YMHT, Coordinator

class TaskCategory(models.Model):
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return self.name

class Task(models.Model):
  PRIORTIY_CHOICES = ((1, 'High'),
                      (2, 'Normal'),
                      (3, 'Low'))

  STATUS_CHOICES = ((1, 'Open'),
                    (2, 'Done'),
                    (3, 'Pending'))

  category = models.ForeignKey(TaskCategory)
  due_date = models.DateField()
  priority = models.IntegerField(choices=PRIORTIY_CHOICES, default=2)
  status = models.IntegerField(choices=STATUS_CHOICES, default=1)
  assigned_to_ymht = models.ForeignKey(YMHT, blank=True, null=True)
  assigned_to_coordinator = models.ForeignKey(Coordinator, blank=True, null=True)

  def __unicode__(self):
    return '%s due by %s' % (self.category, self.due_date)
