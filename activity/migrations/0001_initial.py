# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActivityType'
        db.create_table(u'activity_activitytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'activity', ['ActivityType'])

        # Adding model 'Activity'
        db.create_table(u'activity_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activity.ActivityType'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['place.Place'])),
            ('distance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('difficulty', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hours', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rafting_whitewater', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fishing_shore', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'activity', ['Activity'])


    def backwards(self, orm):
        # Deleting model 'ActivityType'
        db.delete_table(u'activity_activitytype')

        # Deleting model 'Activity'
        db.delete_table(u'activity_activity')


    models = {
        u'activity.activity': {
            'Meta': {'object_name': 'Activity'},
            'difficulty': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fishing_shore': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['place.Place']"}),
            'rafting_whitewater': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activity.ActivityType']"})
        },
        u'activity.activitytype': {
            'Meta': {'object_name': 'ActivityType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'place.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['place.Place']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['activity']