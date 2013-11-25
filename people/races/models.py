from django.db import models
from py2neo import neo4j, node

from general.models import * 

graph_db = neo4j.GraphDatabaseService(neo4j.DEFAULT_URI)

CULTURE_TYPES = ['CLOSED', 'OPEN']
CULTURE_INTERACTION_TYPE=['STATIC', 'EXPANSIONISTIC']
CULTURE_FORM = ['ART', 'TEKNE']

class CultureType(models.Model):
	name = models.TextField()

class CultureInteractionType(models.Model):
	name = models.TextField()

class CultureForm(models.Model):
	name = models.TextField()

class Culture(models.Model):
	culture_type = models.IntegerField(default=0)
	culture_interaction_type = models.IntegerField(default=0)
	culture_form = models.IntegerField(default=0)

class Language(models.Model):
	name = models.TextField()
	secret = models.BooleanField(default=False)
	def __str__(self):
		return self.name

class KlassLanguage(models.Model):
	klass = models.ForeignKey(Klass)
	language = models.ForeignKey(Language)

class Race(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	name = models.TextField()
	mean_death_age = models.IntegerField()
	mean_height = models.IntegerField()
	speed = models.IntegerField()
	skill_points_modifier = models.IntegerField()
	level_adj = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class CharRace(models.Model):
	character = models.ForeignKey(Character, related_name="race", unique=True)
	race = models.ForeignKey(Race, related_name="characters")
	height= models.IntegerField()
	age = models.IntegerField()

	def __str__(self):
		return "%s: %s" %(self.character.name, self.race.name)
	

class RaceLanguage(models.Model):
	race = models.ForeignKey(Race)
	language = models.ForeignKey(Language)

class RaceAbility(models.Model):
	race = models.ForeignKey(Race, related_name="abilities")
	ability = models.ForeignKey(Ability)
	modifier = models.IntegerField()

class RaceFeats(models.Model):
	race = models.ForeignKey(Race, related_name="feats")
	feat = models.ForeignKey(Feat, related_name="races", null=True, blank=True)

class RaceSkills(models.Model):
	race = models.ForeignKey(Race, related_name="skills")
	skill = models.ForeignKey(Skill, related_name="races")
	modifier = models.IntegerField(default=0)