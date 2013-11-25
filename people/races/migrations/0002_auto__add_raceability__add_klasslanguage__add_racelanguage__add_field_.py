# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RaceAbility'
        db.create_table(u'races_raceability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Race'])),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Ability'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'races', ['RaceAbility'])

        # Adding model 'KlassLanguage'
        db.create_table(u'races_klasslanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Klass'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Language'])),
        ))
        db.send_create_signal(u'races', ['KlassLanguage'])

        # Adding model 'RaceLanguage'
        db.create_table(u'races_racelanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Race'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Language'])),
        ))
        db.send_create_signal(u'races', ['RaceLanguage'])

        # Adding field 'Race.mean_death_age'
        db.add_column(u'races_race', 'mean_death_age',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'Race.mean_height'
        db.add_column(u'races_race', 'mean_height',
                      self.gf('django.db.models.fields.IntegerField')(default=180),
                      keep_default=False)

        # Adding field 'Race.speed'
        db.add_column(u'races_race', 'speed',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'Race.skill_points_modifier'
        db.add_column(u'races_race', 'skill_points_modifier',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Language.culture'
        db.delete_column(u'races_language', 'culture_id')

        # Adding field 'Language.name'
        db.add_column(u'races_language', 'name',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'RaceFeats.feat'
        db.alter_column(u'races_racefeats', 'feat_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['general.Feat']))
        # Adding field 'RaceSkills.modifier'
        db.add_column(u'races_raceskills', 'modifier',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'RaceAbility'
        db.delete_table(u'races_raceability')

        # Deleting model 'KlassLanguage'
        db.delete_table(u'races_klasslanguage')

        # Deleting model 'RaceLanguage'
        db.delete_table(u'races_racelanguage')

        # Deleting field 'Race.mean_death_age'
        db.delete_column(u'races_race', 'mean_death_age')

        # Deleting field 'Race.mean_height'
        db.delete_column(u'races_race', 'mean_height')

        # Deleting field 'Race.speed'
        db.delete_column(u'races_race', 'speed')

        # Deleting field 'Race.skill_points_modifier'
        db.delete_column(u'races_race', 'skill_points_modifier')

        # Adding field 'Language.culture'
        db.add_column(u'races_language', 'culture',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['races.Culture']),
                      keep_default=False)

        # Deleting field 'Language.name'
        db.delete_column(u'races_language', 'name')


        # Changing field 'RaceFeats.feat'
        db.alter_column(u'races_racefeats', 'feat_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['general.Feat']))
        # Deleting field 'RaceSkills.modifier'
        db.delete_column(u'races_raceskills', 'modifier')


    models = {
        u'general.ability': {
            'Meta': {'object_name': 'Ability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5'})
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
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'races.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Race']"})
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