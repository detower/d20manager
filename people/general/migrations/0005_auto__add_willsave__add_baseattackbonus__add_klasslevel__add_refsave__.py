# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WillSave'
        db.create_table(u'general_willsave', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.KlassLevel'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'general', ['WillSave'])

        # Adding model 'BaseAttackBonus'
        db.create_table(u'general_baseattackbonus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.KlassLevel'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'general', ['BaseAttackBonus'])

        # Adding model 'KlassLevel'
        db.create_table(u'general_klasslevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruleset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.RuleSet'])),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Klass'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'general', ['KlassLevel'])

        # Adding model 'RefSave'
        db.create_table(u'general_refsave', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.KlassLevel'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'general', ['RefSave'])

        # Adding model 'FortSave'
        db.create_table(u'general_fortsave', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.KlassLevel'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'general', ['FortSave'])

        # Adding model 'SpecialFeat'
        db.create_table(u'general_specialfeat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.KlassLevel'])),
            ('feat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Feat'], null=True, blank=True)),
        ))
        db.send_create_signal(u'general', ['SpecialFeat'])


    def backwards(self, orm):
        # Deleting model 'WillSave'
        db.delete_table(u'general_willsave')

        # Deleting model 'BaseAttackBonus'
        db.delete_table(u'general_baseattackbonus')

        # Deleting model 'KlassLevel'
        db.delete_table(u'general_klasslevel')

        # Deleting model 'RefSave'
        db.delete_table(u'general_refsave')

        # Deleting model 'FortSave'
        db.delete_table(u'general_fortsave')

        # Deleting model 'SpecialFeat'
        db.delete_table(u'general_specialfeat')


    models = {
        u'general.ability': {
            'Meta': {'object_name': 'Ability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'general.baseattackbonus': {
            'Meta': {'object_name': 'BaseAttackBonus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.KlassLevel']"}),
            'modifier': ('django.db.models.fields.IntegerField', [], {})
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
        u'general.fortsave': {
            'Meta': {'object_name': 'FortSave'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.KlassLevel']"}),
            'modifier': ('django.db.models.fields.IntegerField', [], {})
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
        u'general.klasslevel': {
            'Meta': {'object_name': 'KlassLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Klass']"}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'ruleset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.RuleSet']"})
        },
        u'general.klassskill': {
            'Meta': {'object_name': 'KlassSkill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Klass']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Skill']"})
        },
        u'general.refsave': {
            'Meta': {'object_name': 'RefSave'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.KlassLevel']"}),
            'modifier': ('django.db.models.fields.IntegerField', [], {})
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
        },
        u'general.specialfeat': {
            'Meta': {'object_name': 'SpecialFeat'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.Feat']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.KlassLevel']"})
        },
        u'general.willsave': {
            'Meta': {'object_name': 'WillSave'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.KlassLevel']"}),
            'modifier': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['general']