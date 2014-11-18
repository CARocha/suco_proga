# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Caching'
        db.create_table('caching_caching', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('caching', ['Caching'])


    def backwards(self, orm):
        # Deleting model 'Caching'
        db.delete_table('caching_caching')


    models = {
        'caching.caching': {
            'Meta': {'object_name': 'Caching'},
            'activado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['caching']