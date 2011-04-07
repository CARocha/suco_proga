# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Componentes'
        db.create_table('seguridad_componentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('seguridad', ['Componentes'])

        # Adding model 'Alimentos'
        db.create_table('seguridad_alimentos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('componete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seguridad.Componentes'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('seguridad', ['Alimentos'])

        # Adding model 'Seguridad'
        db.create_table('seguridad_seguridad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alimento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seguridad.Alimentos'])),
            ('producen', self.gf('django.db.models.fields.IntegerField')()),
            ('compran', self.gf('django.db.models.fields.IntegerField')()),
            ('consumen', self.gf('django.db.models.fields.IntegerField')()),
            ('consumen_invierno', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('seguridad', ['Seguridad'])

        # Adding model 'Causa'
        db.create_table('seguridad_causa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('seguridad', ['Causa'])

        # Adding model 'Fenomeno'
        db.create_table('seguridad_fenomeno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('causa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seguridad.Causa'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('seguridad', ['Fenomeno'])

        # Adding model 'Graves'
        db.create_table('seguridad_graves', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('seguridad', ['Graves'])

        # Adding model 'Vulnerable'
        db.create_table('seguridad_vulnerable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seguridad.Fenomeno'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('seguridad', ['Vulnerable'])

        # Adding M2M table for field respuesta on 'Vulnerable'
        db.create_table('seguridad_vulnerable_respuesta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vulnerable', models.ForeignKey(orm['seguridad.vulnerable'], null=False)),
            ('graves', models.ForeignKey(orm['seguridad.graves'], null=False))
        ))
        db.create_unique('seguridad_vulnerable_respuesta', ['vulnerable_id', 'graves_id'])

        # Adding model 'PreguntaRiesgo'
        db.create_table('seguridad_preguntariesgo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('seguridad', ['PreguntaRiesgo'])

        # Adding model 'Riesgos'
        db.create_table('seguridad_riesgos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seguridad.PreguntaRiesgo'])),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('seguridad', ['Riesgos'])


    def backwards(self, orm):
        
        # Deleting model 'Componentes'
        db.delete_table('seguridad_componentes')

        # Deleting model 'Alimentos'
        db.delete_table('seguridad_alimentos')

        # Deleting model 'Seguridad'
        db.delete_table('seguridad_seguridad')

        # Deleting model 'Causa'
        db.delete_table('seguridad_causa')

        # Deleting model 'Fenomeno'
        db.delete_table('seguridad_fenomeno')

        # Deleting model 'Graves'
        db.delete_table('seguridad_graves')

        # Deleting model 'Vulnerable'
        db.delete_table('seguridad_vulnerable')

        # Removing M2M table for field respuesta on 'Vulnerable'
        db.delete_table('seguridad_vulnerable_respuesta')

        # Deleting model 'PreguntaRiesgo'
        db.delete_table('seguridad_preguntariesgo')

        # Deleting model 'Riesgos'
        db.delete_table('seguridad_riesgos')


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
        },
        'seguridad.alimentos': {
            'Meta': {'object_name': 'Alimentos'},
            'componete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seguridad.Componentes']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seguridad.causa': {
            'Meta': {'object_name': 'Causa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seguridad.componentes': {
            'Meta': {'object_name': 'Componentes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'seguridad.fenomeno': {
            'Meta': {'object_name': 'Fenomeno'},
            'causa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seguridad.Causa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seguridad.graves': {
            'Meta': {'object_name': 'Graves'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seguridad.preguntariesgo': {
            'Meta': {'object_name': 'PreguntaRiesgo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'seguridad.riesgos': {
            'Meta': {'object_name': 'Riesgos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seguridad.PreguntaRiesgo']"}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'seguridad.seguridad': {
            'Meta': {'object_name': 'Seguridad'},
            'alimento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seguridad.Alimentos']"}),
            'compran': ('django.db.models.fields.IntegerField', [], {}),
            'consumen': ('django.db.models.fields.IntegerField', [], {}),
            'consumen_invierno': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producen': ('django.db.models.fields.IntegerField', [], {})
        },
        'seguridad.vulnerable': {
            'Meta': {'object_name': 'Vulnerable'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seguridad.Fenomeno']"}),
            'respuesta': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['seguridad.Graves']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['seguridad']
