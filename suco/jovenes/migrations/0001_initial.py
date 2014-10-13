# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grupo'
        db.create_table('jovenes_grupo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('jovenes', ['Grupo'])

        # Adding model 'Joven'
        db.create_table('jovenes_joven', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jovenes.Grupo'])),
            ('idseguimiento', self.gf('django.db.models.fields.IntegerField')()),
            ('centroregional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Centroregional'])),
        ))
        db.send_create_signal('jovenes', ['Joven'])


    def backwards(self, orm):
        # Deleting model 'Grupo'
        db.delete_table('jovenes_grupo')

        # Deleting model 'Joven'
        db.delete_table('jovenes_joven')


    models = {
        'jovenes.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jovenes.joven': {
            'Meta': {'object_name': 'Joven'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'centroregional': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Centroregional']"}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jovenes.Grupo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idseguimiento': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.centroregional': {
            'Meta': {'object_name': 'Centroregional'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jovenes']