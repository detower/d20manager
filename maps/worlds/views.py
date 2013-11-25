from django.http import HttpResponse
from django.shortcuts import render_to_response


def list(request):
	return render_to_response('index.html')
def map(request, world, city):
	return render_to_response('index.html')