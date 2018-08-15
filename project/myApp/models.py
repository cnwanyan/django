from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return "%s" % self.gname


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField()
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    #不需要定义主键，在生成时自动添加，并且值会自动添加