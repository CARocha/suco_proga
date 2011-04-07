# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Recolector'
        db.create_table('encuesta_recolector', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['Recolector'])

        # Adding model 'Escolaridad'
        db.create_table('encuesta_escolaridad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['Escolaridad'])

        # Adding model 'Tecnica'
        db.create_table('encuesta_tecnica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['Tecnica'])

        # Adding model 'ParticipacionProyecto'
        db.create_table('encuesta_participacionproyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['ParticipacionProyecto'])

        # Adding model 'Encuesta'
        db.create_table('encuesta_encuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('recolector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Recolector'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('escolaridad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Escolaridad'])),
            ('formacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Tecnica'])),
            ('finca', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comunidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Comunidad'])),
        ))
        db.send_create_signal('encuesta', ['Encuesta'])

        # Adding M2M table for field participacion on 'Encuesta'
        db.create_table('encuesta_encuesta_participacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encuesta', models.ForeignKey(orm['encuesta.encuesta'], null=False)),
            ('participacionproyecto', models.ForeignKey(orm['encuesta.participacionproyecto'], null=False))
        ))
        db.create_unique('encuesta_encuesta_participacion', ['encuesta_id', 'participacionproyecto_id'])


    def backwards(self, orm):
        
        # Deleting model 'Recolector'
        db.delete_table('encuesta_recolector')

        # Deleting model 'Escolaridad'
        db.delete_table('encuesta_escolaridad')

        # Deleting model 'Tecnica'
        db.delete_table('encuesta_tecnica')

        # Deleting model 'ParticipacionProyecto'
        db.delete_table('encuesta_participacionproyecto')

        # Deleting model 'Encuesta'
        db.delete_table('encuesta_encuesta')

        # Removing M2M table for field participacion on 'Encuesta'
        db.delete_table('encuesta_encuesta_participacion')


    models = {
        'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'escolaridad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Escolaridad']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'formacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Tecnica']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ParticipacionProyecto']", 'symmetrical': 'False'}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.escolaridad': {
            'Meta': {'object_name': 'Escolaridad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.participacionproyecto': {
            'Meta': {'object_name': 'ParticipacionProyecto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.tecnica': {
            'Meta': {'object_name': 'Tecnica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['encuesta']
