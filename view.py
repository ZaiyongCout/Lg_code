from django.http import httpResponse
from django.shortcuts import redirect

def index(request):
	pass


def login(request):
	return redirect("/index")
