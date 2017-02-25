from django.db import models

class 	Resturant(models.Model):
	name = models.CharField(max_length = 100)
	phonenumber = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name


class Food(models.Model):
	TASTE_RANK_CHOICES = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
		(7, 7),
		(8, 8),
		(9, 9),
		(10, 10),
	)
	taste_rank_from_one_to_ten = models.IntegerField(choices = TASTE_RANK_CHOICES, null = True)
	name = models.CharField(max_length = 100)
	price = models.IntegerField()
	is_spicy = models.NullBooleanField(null = True)
	comment = models.TextField(max_length = 500, blank = True)
	resturant = models.ForeignKey(Resturant)
	def __unicode__(self):
		return self.name

class Comment(models.Model):
	post_by = models.CharField(max_length = 50)
	email = models.CharField(max_length = 100)
	content = models.TextField(max_length = 1000)
	time = models.DateTimeField()
	resturant = models.ForeignKey(Resturant)

