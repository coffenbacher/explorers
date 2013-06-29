# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'place_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'place', ['Place'])

        # Adding M2M table for field related on 'Place'
        m2m_table_name = db.shorten_name(u'place_place_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_place', models.ForeignKey(orm[u'place.place'], null=False)),
            ('to_place', models.ForeignKey(orm[u'place.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_place_id', 'to_place_id'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'place_place')

        # Removing M2M table for field related on 'Place'
        db.delete_table(db.shorten_name(u'place_place_related'))


    models = {
        u'place.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_rel_+'", 'blank': 'True', 'to': u"orm['place.Place']"})
        }
    }

    complete_apps = ['place']