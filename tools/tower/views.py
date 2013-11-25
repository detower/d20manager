import json
import random

def index(request):
	from django.shortcuts import render_to_response
	return render_to_response('tower.html')

def roll(request):  
	from django.http import HttpResponse
	dice_string = request.REQUEST.get('d')  
	return HttpResponse(json.dumps(do_roll(dice_string)))

def do_roll(dice_string):
	'''
	Rolls the dice of the dice string passed as argument. Returns an object representing the throws and every other useful information
	'''
	if '+' in dice_string:
		dice = dice_string.split('+') #+ are laready ocnverted to spaces  
	else:
		dice = dice_string.split()
	response = {}
	response['querystring'] = dice_string.replace(' ', '+')
	response['type'] = "response"
	require ={}
	fixed = 0    

	for die in dice:        
		itms = die.split('d')        
		if len(itms)>1:
			if itms[1] == "%":
				a=0
				try:                    
					a = require['10']
				except:
					pass
				require['%']=a + int(itms[0])
			else:
				try:
					int(itms[1])
				except:
					return {"type":"error", "message":"Wrong Syntax", "item":die }
				a=0
				try:
					a = require[itms[1]]
				except:
					pass
				require[itms[1]]=a + int(itms[0])
		else:
			fixed = fixed + int(itms[0])
	response['parsed_throws'] = require
	response['parsed_fixed'] = fixed

	result = fixed
	results = {}
	for die,throws in require.items():
		for i in range(0,throws):
			if die == "%":
				tens = random.randint(0,9)
				units = random.randint(0,9)
				var = tens * 10 + units
				stuff = [tens, units, var]
			elif die == "10":
				var = random.randint(0,9)
				stuff = var
			else:
				var = random.randint(1,int(die))
				stuff = var
			if var <1:
				var = 1
			result = result + var
			if die not in results:
				results[die] = []
			results[die].append(stuff)


	response['result'] = result
	response['results'] = results

	return response

