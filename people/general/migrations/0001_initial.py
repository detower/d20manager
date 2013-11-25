# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RuleSet'
        db.create_table(u'general_ruleset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'general', ['RuleSet'])

        # Adding model 'Ability'
        db.create_table(u'general_ability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'general', ['Ability'])

        # Adding model 'Skill'
        db.create_table(u'general_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Ability'])),
            ('trained_only', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('action', self.gf('django.db.models.fields.FloatField')(default=1)),
        ))
        db.send_create_signal(u'general', ['Skill'])

        # Adding model 'SkillSynergy'
        db.create_table(u'general_skillsynergy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('activator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activates', to=orm['general.Skill'])),
            ('activator_ranks', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('activated', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_activated_by', to=orm['general.Skill'])),
            ('activated_modifier', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'general', ['SkillSynergy'])

        # Adding model 'Klass'
        db.create_table(u'general_klass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('allowed_alignment_lawful_min', self.gf('django.db.models.fields.FloatField')(default=-1000)),
            ('allowed_alignment_lawful_max', self.gf('django.db.models.fields.FloatField')(default=1000)),
            ('allowed_alignment_indole_min', self.gf('django.db.models.fields.FloatField')(default=-1000)),
            ('allowed_alignment_indole_max', self.gf('django.db.models.fields.FloatField')(default=1000)),
            ('hit_die', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'general', ['Klass'])

        # Adding model 'KlassSkill'
        db.create_table(u'general_klassskill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Klass'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Skill'])),
        ))
        db.send_create_signal(u'general', ['KlassSkill'])

        # Adding model 'Character'
        db.create_table(u'general_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alignment_lawfulness', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('alignment_indole', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'general', ['Character'])

        # Adding model 'CharAbility'
        db.create_table(u'general_charability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='abilities', to=orm['general.Character'])),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Ability'])),
            ('base_value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'general', ['CharAbility'])


    def backwards(self, orm):
        # Deleting model 'RuleSet'
        db.delete_table(u'general_ruleset')

        # Deleting model 'Ability'
        db.delete_table(u'general_ability')

        # Deleting model 'Skill'
        db.delete_table(u'general_skill')

        # Deleting model 'SkillSynergy'
        db.delete_table(u'general_skillsynergy')

        # Deleting model 'Klass'
        db.delete_table(u'general_klass')

        # Deleting model 'KlassSkill'
        db.delete_table(u'general_klassskill')

        # Deleting model 'Character'
        db.delete_table(u'general_character')

        # Deleting model 'CharAbility'
        db.delete_table(u'general_charability')


    models = {
        u'general.ability': {
            'Meta': {'object_name': 'Ability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'general.charability': {
            'Meta': {'object_name': 'CharAbility'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Ability']"}),
            'base_value': ('django.db.models.fields.IntegerField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abilities'", 'to': u"orm['general.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
        },
        u'general.character': {
            'Meta': {'object_name': 'Character'},
            'alignment_indole': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'alignment_lawfulness': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
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
        u'general.klassskill': {
            'Meta': {'object_name': 'KlassSkill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Klass']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Skill']"})
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
        u'general.skillsynergy': {
            'Meta': {'object_name': 'SkillSynergy'},
            'activated': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_activated_by'", 'to': u"orm['general.Skill']"}),
            'activated_modifier': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'activator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activates'", 'to': u"orm['general.Skill']"}),
            'activator_ranks': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
        }
    }

    complete_apps = ['general']