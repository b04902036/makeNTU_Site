from django.shortcuts import render, get_object_or_404
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Bike, User, Slot
from django.utils.timezone import utc
from datetime import datetime
import os
def time(request):
	allBike = Bike.objects.all()
	y = []
	for bike in allBike:
		if bike.status == 1:
			y.append(bike)
	now = datetime.now()
	for bike in y:
		preDiff = now - bike.time.replace(tzinfo=None)
		bike.diffTime = preDiff.days
	sorted(y, key = lambda car : car.diffTime)
	t = template.loader.get_template('time.html')
	d = template.RequestContext(request, locals())
	return HttpResponse(t.render(d))
def empty_slot(request):
	x = []
	places = Slot.objects.all()
	for place in places:
		if place.vacancy == True:
			x.append(place)
	t = template.loader.get_template('empty_slot.html')
	d = template.RequestContext(request, locals())
	return HttpResponse(t.render(d))

def find_bike(request):
	now_dir = os.path.dirname(__file__)
	file_path = os.path.join(now_dir, 'id.txt')
	f = open(file_path)
	for line in f:
		num = line.split()
		id = num[0]
		x = num[1]
		y = num[2]
		num = Bike.objects.filter(myId = id).count()
		if num == 0:
			return HttpResponseRedirect('/menu/')
		bike = Bike.objects.get(myId = id)
		if x == 0:
			bike.status = 0
		else:
			bike.status = 1
		bike.x = x
		bike.y = y
		bike.save()
	if request.POST:
		name = request.POST['name']
		theUser = User.objects.get(name = name)
	data = f.read()
	bikes = Bike.objects.all()
	jason = [0, 50]
	t = template.loader.get_template('find_bike.html')
	d = template.RequestContext(request, locals())
	return HttpResponse(t.render(d))
def menu(request):
	t = template.loader.get_template('menu.html')
	if request.POST:
		myId = request.POST['myId']
		myName = request.POST['myName']
		num = User.objects.filter(name = myName).count()
		if num == 0:
			user = User.objects.create(name = myName)
		else:
			user = User.objects.get(name = myName)
		num = Bike.objects.filter(myId = myId).count()
		if num == 0:
			theBike = Bike.objects.create(myId = myId, user = user)
		else:
			theBike = Bike.objects.get(myId = myId)
		theBike.time = datetime.datetime.now()
		theBike.save()
	d = template.RequestContext(request, locals())
	return HttpResponse(t.render(d))
