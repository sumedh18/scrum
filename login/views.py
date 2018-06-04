from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.
def main_page(request):
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)

def logout(request):
	logout(request)
	return HttpResponseRediect('/')
def login(request):
	return HttpResponseRediect('/registration/login.html')