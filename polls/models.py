from django.db import models
from django.utils import timezone
import datetime  

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        date = timezone.now() - datetime.timedelta(days=1)
        return self.pub_date >= date
        
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text
    