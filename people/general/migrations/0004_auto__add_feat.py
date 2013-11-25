# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feat'
        db.create_table(u'general_feat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'general', ['Feat'])


    def backwards(self, orm):
        # Deleting model 'Feat'
        db.delete_table(u'general_feat')


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
        u'general.charklass': {
            'Meta': {'object_name': 'CharKlass'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'klasses'", 'to': u"orm['general.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chars'", 'to': u"orm['general.Klass']"})
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