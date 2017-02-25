from django.db import models

class Date(models.Model):
	time = models.CharField(max_length = 100)

class Link(models.Model):
	title_for_link = models.CharField(max_length = 100)
	href = models.CharField(max_length = 100)

class Frenchnote(models.Model):
	content = models.TextField(max_length = 10000)
	title = models.CharField(max_length = 1000)
	date = models.ForeignKey(Date)

