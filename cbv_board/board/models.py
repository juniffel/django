from django.db import models
from django.utils import timezone


class Board(models.Model):
  title = models.CharField(max_length=50)
  writer = models.CharField(max_length=30)
  content = models.TextField()
  regdate = models.DateTimeField(auto_now = timezone.now)
  readcount = models.IntegerField(default=0)

  def __str__(self):
    return '%s,%s(%d)' %(self.title, self.writer, self.readcount)

  # 조회수 증가 체크
  def increment_read_count(self):
    self.readcount +=1
    self.save()