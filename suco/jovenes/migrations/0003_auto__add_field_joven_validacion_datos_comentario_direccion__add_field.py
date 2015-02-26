# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Joven.validacion_datos_comentario_direccion'
        db.add_column('jovenes_joven', 'validacion_datos_comentario_direccion',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Joven.validacion_datos_comentario_centro'
        db.add_column('jovenes_joven', 'validacion_datos_comentario_centro',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Joven.validacion_datos_comentario_direccion'
        db.delete_column('jovenes_joven', 'validacion_datos_comentario_direccion')

        # Deleting field 'Joven.validacion_datos_comentario_centro'
        db.delete_column('jovenes_joven', 'validacion_datos_comentario_centro')


    models = {
        'jovenes.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jovenes.joven': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Joven'},
            'activo': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'centroregional': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Centroregional']"}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jovenes.Grupo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idseguimiento': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'validacion_datos_comentario_centro': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'validacion_datos_comentario_direccion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'lugar.centroregional': {
            'Meta': {'object_name': 'Centroregional'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jovenes']