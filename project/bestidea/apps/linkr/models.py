from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Item(models.Model):
	url = models.URLField(verify_exists=False,max_length=2000)
	desc= models.TextField('URL Description')
	created= models.DateTimeField('date created', auto_now_add=True)
	modified=models.DateTimeField('date modified',auto_now=True)
	topics = models.ManyToManyField("Topic",related_name='items')
	
	def __unicode__(self):
		return self.url
	
class Topic(models.Model):
	name=models.CharField(max_length=200)
	desc=models.TextField('Topic Description')
	created= models.DateTimeField('date created', auto_now_add=True)
	modified=models.DateTimeField('date modified',auto_now=True)
	#items = models.ManyToManyField("Item", blank=True) 
	user = models.ForeignKey(User, related_name='+')
	
	def was_published_recently(self):
		return self.created >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.name
