from django import template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
def welcome(request):
	t = template.loader.get_template('welcome.html')
	if request.GET:
		if 'username' in request.COOKIES and str(request.GET['username']) == str(request.COOKIES['username']):
			return HttpResponse('Welcome back! {0}'. format(request.GET['username'])) 
		
		c = template.Context(locals())	
		if 'username' in request.GET and request.GET['username'] != '':
			response = HttpResponse('Welcome!' + request.GET['username'])
			response.set_cookie('username', request.GET['username'])
			return response
	else:
		return HttpResponse(t.render(c))
