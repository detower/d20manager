from django.db import models
from django.db.models import Count, Min, Sum, Avg
import math
from races.models import *

class RuleSet(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Feat(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.name

class Ability(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	name=models.CharField(max_length=100)
	short = models.CharField(max_length=5)

	def __str__(self):
		return str(self.ruleset) + "-" + self.name

class Skill(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	name=models.CharField(max_length=100)
	ability = models.ForeignKey(Ability)
	trained_only = models.BooleanField(default=True)
	action = models.FloatField(default=1)
	try_again = models.BooleanField(default=True)	
	ac_penalty = models.BooleanField(default=False)

	def __str__(self):
		return str(self.ruleset) + "-" + self.name

class FeatSkill(models.Model):
	feat = models.ForeignKey(Feat)
	skill = models.ForeignKey(Skill)
	modifier = models.IntegerField(default=2)


class SkillSynergy(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	activator = models.ForeignKey(Skill, related_name="activates")
	activator_ranks = models.IntegerField(default=5)
	activated = models.ForeignKey(Skill, related_name="is_activated_by")
	activated_modifier = models.IntegerField(default=2)
	def __str__(self):
		return str(self.activator) + " --> " + str(self.activated)

class Klass(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	name = models.CharField(max_length=255)
	allowed_alignment_lawful_min=models.FloatField(default=-1000)
	allowed_alignment_lawful_max=models.FloatField(default=1000)
	allowed_alignment_indole_min=models.FloatField(default=-1000)
	allowed_alignment_indole_max=models.FloatField(default=1000)
	hit_die=models.CharField(max_length=50)
	def __str__(self):
		return str(self.ruleset) + "-" + self.name

class KlassLevel(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	klass = models.ForeignKey(Klass)
	level = models.IntegerField()

	def __str__(self):
		return "%s - %s" % (self.klass.name, self.level)

class BaseAttackBonus(models.Model):
	klass_level = models.ForeignKey(KlassLevel,related_name="base_attack_bonus", unique=True)
	modifier = models.IntegerField()

class FortSave(models.Model):
	klass_level = models.ForeignKey(KlassLevel,related_name="fort_save", unique=True)
	modifier = models.IntegerField()

class RefSave(models.Model):
	klass_level = models.ForeignKey(KlassLevel,related_name="ref_save", unique=True)
	modifier = models.IntegerField()

class WillSave(models.Model):
	klass_level = models.ForeignKey(KlassLevel,related_name="will_save", unique=True)
	modifier = models.IntegerField()

class SpecialFeat(models.Model):
	klass_level = models.ForeignKey(KlassLevel, related_name="feats")
	feat = models.ForeignKey(Feat, null=True, blank=True, related_name="klass_spec")

class KlassSkill(models.Model):
	klass=models.ForeignKey(Klass, related_name="skills")
	skill = models.ForeignKey(Skill, related_name="klass_spec")
	def __str__(self):
		return str(self.klass) + " --> " + str(self.skill)

class Character(models.Model):
	ruleset = models.ForeignKey(RuleSet)

	name = models.CharField(max_length=255)

	#klass = models.ForeignKey(Klass)
	alignment_lawfulness = models.FloatField(default=0)
	alignment_indole = models.FloatField(default=0)

	@property
	def alignment_lawfulness_str(self):
		if self.alignment_lawfulness <-333:
			return "chaotic"
		elif self.alignment_lawfulness < 333:
			return "neutral"
		else:
			return "lawful" 
	@property
	def alignment_indole_str(self):
		if self.alignment_indole <-333:
			return "evil"
		elif self.alignment_indole < 333:
			return "neutral"
		else:
			return "good"

	def __str__(self):
		return " %s - alignment: %s %s" % (self.name, self.alignment_lawfulness_str, self.alignment_indole_str)


	@property
	def klass(self):
		return CharKlass.objects.filter(character = self).distinct('klass')
	
	@property
	def level(self):
		return self.klasses.count()

	@property
	def all_feats(self):
		q = Feat.objects.none()

	@property
	def skills(self):
		base = Skill.objects.filter(trained_only=False)
		for k in self.klass:
			base = base | Skill.objects.filter(id__in = k.klass.skills.values_list('id', flat=True))
		for k in CharSkill.objects.filter(character=self).distinct('skill'):
			base = base | Skill.objects.filter(id = k.skill.id)

		ret = []
		for skill in base:
			charpoints = CharSkill.objects.filter(character = self, skill=skill).aggregate(Sum('points'))['points__sum']
			if charpoints is None:
				charpoints = 0
			val = self.abilities.filter(ability= skill.ability)
			if val.count()>0:
				val = val[0].modifier + charpoints
			else:
				val = charpoints
			ret.append({'skill' : skill.name,
						'ability':skill.ability.short,
						'value' : val
							  #CharSkill.objects.filter(character = self, skill=skill).aggregate(Sum('points')).values_list('points__sum', flat=True)[0]
			})
		return ret

class CharKlass(models.Model):
	character = models.ForeignKey(Character, related_name="klasses")
	klass = models.ForeignKey(Klass, related_name="chars")

	@property
	def level(self):
		return CharKlass.objects.filter(character = self.character, klass=self.klass).count()

	@property
	def levels(self):
		return KlassLevel.objects.filter(klass = self.klass, level__lte = self.level)

	@property
	def details(self):
		return KlassLevel.objects.get(klass = self.klass, level = self.level)


	@property
	def feats(self):
		return Feat.objects.filter(klass_spec=SpecialFeat.objects.filter(klass_level__in=KlassLevel.objects.filter(klass = self.klass, level__lte= self.level)))

	@property
	def skills(self):
		return Skill.objects.filter(klass_spec=KlassSkill.objects.filter(klass=self.klass))


class CharAbility(models.Model):
	ruleset = models.ForeignKey(RuleSet)
	character = models.ForeignKey(Character, related_name="abilities")
	ability = models.ForeignKey(Ability)
	base_value = models.IntegerField()
	alter_value = models.IntegerField(default=0)

	@property
	def altered_value(self):
		a = self.character.race.all()[0]
		b = a.race.abilities.filter(ability = self.ability)
		if b.count() > 0:
			b = b[0].modifier
		else:
			b = 0
		return b

	@property
	def value(self):
		av = self.altered_value
		return self.base_value+av
	
	@property
	def modifier(self):
		return int(math.floor((self.value-10)/float(2)))

	def __str__(self):
		return "%s-%s" % (self.character.name, self.ability.name)

	class Meta:
		ordering=['ability__name']

class CharSkill(models.Model):
	character = models.ForeignKey(Character)
	skill = models.ForeignKey(Skill)
	points = models.IntegerField()

	def __str__(self):
		return "%s:%s=%s" % (self.character.name, self.skill.name, self.points)
