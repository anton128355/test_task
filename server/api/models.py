from django.db import models


class Log(models.Model):
  name = models.CharField(max_length=30, null=True)
  surname = models.CharField(max_length=30, null=True)
  uuid = models.CharField(max_length=30, null=True)
  plate_number = models.CharField(max_length=30, null=True)
  group = models.CharField(max_length=30, null=True)
  date = models.CharField(max_length=30, null=True)
  direction = models.CharField(max_length=30, null=True)
  status = models.CharField(max_length=5, null=True)
  type_passage = models.CharField(max_length=5, null=True)
  photo = models.CharField(max_length=30, null=True)
  sync = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.name + " " + self.surname
