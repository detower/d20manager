from django.db import models

class Adventure(models.Model):
	name = models.TextField()
	description = models.TextField()
	date_start = models.TextField()
	location_start = models.TextField()

class AdvetureWorld(models.Model):
	adventure = models.ForeignKey(Adventure)
	world = models.IntegerField()

class Player(models.Model):
	adventure = models.ForeignKey(Adventure)
	user = models.ForeignKey(User)
	char = models.IntegerField()

class CharacterPosition(models.Model):
	moment = models.DateTimeField(auto_now=True)
	character = models.IntegerField()
	character_dump = models.TextField()
	world = models.IntegerField()
	lon = models.FloatField()
	lat = models.FloatField()
	alt = models.FloatField(default=0)

class Master(models.Model):
	adventure = models.ForeignKey(Adventure)
	player = models.ForeignKey(User)

class Quest(models.Model):
	author = models.ForeignKey(User)
	name = models.TextField()
	description= models.TextField()

class QuestCharacter(models.Model)
	quest = models.ForeignKey(Quest)
	character = models.IntegerField()

class QuestWorld(models.Model):
	quest = models.ForeignKey(Quest)
	world = models.IntegerField()

class QuestLocation(models.Model):
	quest = models.ForeignKey(Quest)
	location = models.IntegerField()
	world = models.IntegerField()
	description = models.TextField()




