from django.shortcuts import render
from .models import Card
# Create your views here.
def hello(request):
	return render(request, 'scrum/home.html',{})