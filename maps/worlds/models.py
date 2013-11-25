from django.db import models

# Create your models here.
class World(models.Model):
	name = models.TextField()

class RacesLanguage(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.TextField()
	secret = models.BooleanField()
	class Meta:
		db_table = 'races_language'

class RacesRace(models.Model):
	id = models.IntegerField(primary_key=True)
	ruleset_id = models.IntegerField()
	name = models.TextField()
	mean_death_age = models.IntegerField()
	mean_height = models.IntegerField()
	speed = models.IntegerField()
	skill_points_modifier = models.IntegerField()
	level_adj = models.IntegerField()
	class Meta:
		db_table = 'races_race'

class Racelanguage(models.Model):
	id = models.IntegerField(primary_key=True)
	race = models.ForeignKey(RacesRace)
	language = models.ForeignKey(RacesLanguage)
	class Meta:
		db_table = 'races_racelanguage'
