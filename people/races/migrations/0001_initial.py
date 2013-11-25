# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CultureType'
        db.create_table(u'races_culturetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'races', ['CultureType'])

        # Adding model 'CultureInteractionType'
        db.create_table(u'races_cultureinteractiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'races', ['CultureInteractionType'])

        # Adding model 'CultureForm'
        db.create_table(u'races_cultureform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'races', ['CultureForm'])

        # Adding model 'Culture'
        db.create_table(u'races_culture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('culture_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('culture_interaction_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('culture_form', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'races', ['Culture'])

        # Adding model 'Language'
        db.create_table(u'races_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('culture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['races.Culture'])),
        ))
        db.send_create_signal(u'races', ['Language'])

        # Adding model 'Race'
        db.create_table(u'races_race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'races', ['Race'])

        # Adding model 'RaceFeats'
        db.create_table(u'races_racefeats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feats', to=orm['races.Race'])),
            ('feat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='races', to=orm['general.Feat'])),
        ))
        db.send_create_signal(u'races', ['RaceFeats'])

        # Adding model 'RaceSkills'
        db.create_table(u'races_raceskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skills', to=orm['races.Race'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name='races', to=orm['general.Skill'])),
        ))
        db.send_create_signal(u'races', ['RaceSkills'])


    def backwards(self, orm):
        # Deleting model 'CultureType'
        db.delete_table(u'races_culturetype')

        # Deleting model 'CultureInteractionType'
        db.delete_table(u'races_cultureinteractiontype')

        # Deleting model 'CultureForm'
        db.delete_table(u'races_cultureform')

        # Deleting model 'Culture'
        db.delete_table(u'races_culture')

        # Deleting model 'Language'
        db.delete_table(u'races_language')

        # Deleting model 'Race'
        db.delete_table(u'races_race')

        # Deleting model 'RaceFeats'
        db.delete_table(u'races_racefeats')

        # Deleting model 'RaceSkills'
        db.delete_table(u'races_raceskills')


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
        u'races.language': {
            'Meta': {'object_name': 'Language'},
            'culture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['races.Culture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'races.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
        },
        u'races.racefeats': {
            'Meta': {'object_name': 'RaceFeats'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'races'", 'to': u"orm['general.Feat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feats'", 'to': u"orm['races.Race']"})
        },
        u'races.raceskills': {
            'Meta': {'object_name': 'RaceSkills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': u"orm['races.Race']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'races'", 'to': u"orm['general.Skill']"})
        }
    }

    complete_apps = ['races']