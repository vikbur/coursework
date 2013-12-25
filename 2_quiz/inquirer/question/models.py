from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.question


class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=50)
    voted = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice
