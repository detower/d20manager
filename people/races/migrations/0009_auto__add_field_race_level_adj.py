# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Race.level_adj'
        db.add_column(u'races_race', 'level_adj',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Race.level_adj'
        db.delete_column(u'races_race', 'level_adj')


    models = {
        u'general.ability': {
            'Meta': {'object_name': 'Ability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'general.character': {
            'Meta': {'object_name': 'Character'},
            'alignment_indole': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'alignment_lawfulness': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
        },
        u'general.feat': {
            'Meta': {'object_name': 'Feat'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'general.klass': {
            'Meta': {'object_name': 'Klass'},
            'allowed_alignment_indole_max': ('django.db.models.fields.FloatField', [], {'default': '1000'}),
            'allowed_alignment_indole_min': ('django.db.models.fields.FloatField', [], {'default': '-1000'}),
            'allowed_alignment_lawful_max': ('django.db.models.fields.FloatField', [], {'default': '1000'}),
            'allowed_alignment_lawful_min': ('django.db.models.fields.FloatField', [], {'default': '-1000'}),
            'hit_die': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
        },
        u'general.ruleset': {
            'Meta': {'object_name': 'RuleSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'general.skill': {
            'Meta': {'object_name': 'Skill'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Ability']"}),
            'action': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"}),
            'trained_only': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'races.charrace': {
            'Meta': {'object_name': 'CharRace'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'race'", 'unique': 'True', 'to': u"orm['general.Character']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': u"orm['races.Race']"})
        },
        u'races.culture': {
            'Meta': {'object_name': 'Culture'},
            'culture_form': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'culture_interaction_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'culture_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'races.cultureform': {
            'Meta': {'object_name': 'CultureForm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'races.cultureinteractiontype': {
            'Meta': {'object_name': 'CultureInteractionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'races.culturetype': {
            'Meta': {'object_name': 'CultureType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'races.klasslanguage': {
            'Meta': {'object_name': 'KlassLanguage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Klass']"}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Language']"})
        },
        u'races.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'secret': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'races.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_adj': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mean_death_age': ('django.db.models.fields.IntegerField', [], {}),
            'mean_height': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"}),
            'skill_points_modifier': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {})
        },
        u'races.raceability': {
            'Meta': {'object_name': 'RaceAbility'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Ability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abilities'", 'to': u"orm['races.Race']"})
        },
        u'races.racefeats': {
            'Meta': {'object_name': 'RaceFeats'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'races'", 'null': 'True', 'to': u"orm['general.Feat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feats'", 'to': u"orm['races.Race']"})
        },
        u'races.racelanguage': {
            'Meta': {'object_name': 'RaceLanguage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Language']"}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Race']"})
        },
        u'races.raceskills': {
            'Meta': {'object_name': 'RaceSkills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': u"orm['races.Race']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'races'", 'to': u"orm['general.Skill']"})
        }
    }

    complete_apps = ['races']