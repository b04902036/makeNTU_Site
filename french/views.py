from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import Date, Frenchnote, Link
from forms import FrenchNoteForm, FrenchMenuForm
# Create your views here.
def french_menu(request):
	t = template.loader.get_template('frenchmenu.html')
	if request.POST:
		if 'time' in request.POST and request.POST['time'] != '':
			time = request.POST['time']
			date = Date.objects.create(time = time)
		if 'href' in request.POST and request.POST['href'] != '':
			href = request.POST['href']
			title_for_link = request.POST['title_for_link']
			link = Link.objects.create(href = href, title_for_link = title_for_link)
	dates = Date.objects.all()
	links = Link.objects.all()
	form = FrenchMenuForm()
	requestURL = request.path_info
	c = template.RequestContext(request, locals())
	return HttpResponse(t.render(c))
def french_note(request, id):
	date = Date.objects.get(id = id)
	if request.POST and 'content' in request.POST and request.POST['content'] != '':
		title = request.POST['title']
		content = request.POST['content']
		Frenchnote.objects.create(title = title, content = content, date = date)
	form = FrenchNoteForm().as_table
	requestURL = request.path_info
	t = template.loader.get_template('french_note.html')
	c = template.RequestContext(request, locals())
	return HttpResponse(t.render(c))
def french_note_submit(request):
	requestURL = request.GET['url']
	form = FrenchNoteForm().as_table
	t = template.loader.gett_template('french_note_submit.html')
	c = template.RequestContext(request, locals())
	return HttpResponse(t.render(c))

def french_delete(request):
	t = template.loader.get_template('french_delete.html')
	requestURL = request.GET['url']
	if request.GET:
		id = request.GET['id']
		if str(request.GET['type']) == 'date':
			date = Date.objects.get(id = id)
			date.delete()
		if str(request.GET['type']) == 'link':
			link = Link.objects.get(id = id)
			link.delete()
		if str(request.GET['type']) == 'note':
			note = Frenchnote.objects.get(id = id)
			note.delete()
	else:
		return HttpResponseRedirect('%s' % requestURL)
	c = template.Context(locals())
	return HttpResponse(t.render(c))
#def frenchnote(request, id):