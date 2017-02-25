from django.shortcuts import render
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from resturants.models import Resturant, Food, Comment
from django.utils import timezone
from forms import CommentForm
def menu(request):
	if 'name' in request.GET and request.GET['name'] != '':
		resturant = Resturant.objects.get(name = request.GET['name'])
	else:
		return HttpResponseRedirect('/resturants_list/')
	d = template.Context(locals())
	t = template.loader.get_template('menu_for_one.html')
	return HttpResponse(t.render(d))

def resturants_list(request):
	resturants = Resturant.objects.all()
	t = template.loader.get_template('resturants_list.html')
	c = template.Context(locals())
	return HttpResponse(t.render(c))

def comment(request, id):
	if id:
		resturant = Resturant.objects.get(id = id)
	else:
		return HttpResponseRedirect('/resturants_list/')
	if request.POST:
		post_by = request.POST['post_by']
		email = request.POST['email']
		content = request.POST['comment']
		time = timezone.localtime(timezone.now())
		r = resturant
		x = Comment.objects.create(post_by = post_by, content = content, email = email, time = time, resturant = r)
	requestURL = request.path
	form = CommentForm().as_table
	t = template.loader.get_template('comment.html')
	c = template.RequestContext(request, locals())
	return HttpResponse(t.render(c))

def comment_delete(request):
	if 'comment_id' in request.GET and request.GET['comment_id']:
		comment = Comment.objects.get(id = request.GET['comment_id'])
		comment.delete()
		x = True
	else:
		x = False
	url = request.GET.get('url', False)
	t = template.loader.get_template('comment_delete.html')
	c = template.Context(locals())
	return HttpResponse(t.render(c))