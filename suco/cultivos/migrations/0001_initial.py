# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pastos'
        db.create_table('cultivos_pastos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('cultivos', ['Pastos'])

        # Adding model 'CultivoPasto'
        db.create_table('cultivos_cultivopasto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cultivos.Pastos'])),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('cultivos', ['CultivoPasto'])

        # Adding model 'Componente'
        db.create_table('cultivos_componente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('cultivos', ['Componente'])

        # Adding model 'TipoCultivos'
        db.create_table('cultivos_tipocultivos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cultivos.Componente'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('cultivos', ['TipoCultivos'])

        # Adding model 'Cultivos'
        db.create_table('cultivos_cultivos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cultivos.TipoCultivos'])),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('consumo', self.gf('django.db.models.fields.FloatField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('venta_organizada', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('cultivos', ['Cultivos'])

        # Adding M2M table for field venta_libre on 'Cultivos'
        db.create_table('cultivos_cultivos_venta_libre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cultivos', models.ForeignKey(orm['cultivos.cultivos'], null=False)),
            ('aquienvende', models.ForeignKey(orm['animal_produccion.aquienvende'], null=False))
        ))
        db.create_unique('cultivos_cultivos_venta_libre', ['cultivos_id', 'aquienvende_id'])


    def backwards(self, orm):
        
        # Deleting model 'Pastos'
        db.delete_table('cultivos_pastos')

        # Deleting model 'CultivoPasto'
        db.delete_table('cultivos_cultivopasto')

        # Deleting model 'Componente'
        db.delete_table('cultivos_componente')

        # Deleting model 'TipoCultivos'
        db.delete_table('cultivos_tipocultivos')

        # Deleting model 'Cultivos'
        db.delete_table('cultivos_cultivos')

        # Removing M2M table for field venta_libre on 'Cultivos'
        db.delete_table('cultivos_cultivos_venta_libre')


    models = {
        'animal_produccion.aquienvende': {
            'Meta': {'object_name': 'AquienVende'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'cultivos.componente': {
            'Meta': {'object_name': 'Componente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'cultivos.cultivopasto': {
            'Meta': {'object_name': 'CultivoPasto'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cultivos.Pastos']"})
        },
        'cultivos.cultivos': {
            'Meta': {'object_name': 'Cultivos'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'consumo': ('django.db.models.fields.FloatField', [], {}),
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cultivos.TipoCultivos']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'venta_libre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['animal_produccion.AquienVende']", 'symmetrical': 'False'}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        'cultivos.pastos': {
            'Meta': {'object_name': 'Pastos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'cultivos.tipocultivos': {
            'Meta': {'object_name': 'TipoCultivos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cultivos.Componente']"}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
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

    complete_apps = ['cultivos']
