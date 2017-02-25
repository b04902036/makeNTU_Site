from django.db import models

class User(models.Model):
	name = models.CharField(max_length = 100)

class Bike(models.Model):
	myId = models.CharField(max_length = 100)
	user = models.ForeignKey(User)
	x = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0)
	y = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0)
	status = models.BigIntegerField(default = 0)

class Slot(models.Model):
	x = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0)
	y = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0)
	vacancy = models.BooleanField(default = True)

class showFile(models.Model):
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name

class Line(models.Model):
	line = models.CharField(max_length = 100)
	file = models.ForeignKey(showFile)
