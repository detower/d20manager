from django.shortcuts import render_to_response
from .models import *

def char_sheet(request, ruleset_id, character_id, character_name):
	char = Character.objects.get(ruleset_id = ruleset_id, id=character_id)
	return render_to_response('charsheet.html', {'char':char})

def create(request):
	pass

def manual_race(request, ruleset_id, race_id):
	pass


def manual_class(request, ruleset_id, race_id):
	pass

def manual_feat(request, ruleset_id, race_id):
	pass

def manual_skill(request, ruleset_id, race_id):
	pass