# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Animales'
        db.create_table('animal_produccion_animales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('animal_produccion', ['Animales'])

        # Adding model 'ProductoAnimal'
        db.create_table('animal_produccion_productoanimal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('animal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animal_produccion.Animales'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('animal_produccion', ['ProductoAnimal'])

        # Adding model 'AnimalesFinca'
        db.create_table('animal_produccion_animalesfinca', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('animales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animal_produccion.Animales'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('valor', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('animal_produccion', ['AnimalesFinca'])

        # Adding model 'AquienVende'
        db.create_table('animal_produccion_aquienvende', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('animal_produccion', ['AquienVende'])

        # Adding model 'ProduccionConsumo'
        db.create_table('animal_produccion_produccionconsumo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animal_produccion.ProductoAnimal'])),
            ('total_produccion', self.gf('django.db.models.fields.IntegerField')()),
            ('consumo', self.gf('django.db.models.fields.FloatField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('venta_organizada', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('animal_produccion', ['ProduccionConsumo'])

        # Adding M2M table for field venta_libre on 'ProduccionConsumo'
        db.create_table('animal_produccion_produccionconsumo_venta_libre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produccionconsumo', models.ForeignKey(orm['animal_produccion.produccionconsumo'], null=False)),
            ('aquienvende', models.ForeignKey(orm['animal_produccion.aquienvende'], null=False))
        ))
        db.create_unique('animal_produccion_produccionconsumo_venta_libre', ['produccionconsumo_id', 'aquienvende_id'])


    def backwards(self, orm):
        
        # Deleting model 'Animales'
        db.delete_table('animal_produccion_animales')

        # Deleting model 'ProductoAnimal'
        db.delete_table('animal_produccion_productoanimal')

        # Deleting model 'AnimalesFinca'
        db.delete_table('animal_produccion_animalesfinca')

        # Deleting model 'AquienVende'
        db.delete_table('animal_produccion_aquienvende')

        # Deleting model 'ProduccionConsumo'
        db.delete_table('animal_produccion_produccionconsumo')

        # Removing M2M table for field venta_libre on 'ProduccionConsumo'
        db.delete_table('animal_produccion_produccionconsumo_venta_libre')


    models = {
        'animal_produccion.animales': {
            'Meta': {'object_name': 'Animales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'animal_produccion.animalesfinca': {
            'Meta': {'object_name': 'AnimalesFinca'},
            'animales': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['animal_produccion.Animales']"}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {})
        },
        'animal_produccion.aquienvende': {
            'Meta': {'object_name': 'AquienVende'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'animal_produccion.produccionconsumo': {
            'Meta': {'object_name': 'ProduccionConsumo'},
            'consumo': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['animal_produccion.ProductoAnimal']"}),
            'total_produccion': ('django.db.models.fields.IntegerField', [], {}),
            'venta_libre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['animal_produccion.AquienVende']", 'symmetrical': 'False'}),
            'venta_organizada': ('django.db.models.fields.FloatField', [], {})
        },
        'animal_produccion.productoanimal': {
            'Meta': {'object_name': 'ProductoAnimal'},
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['animal_produccion.Animales']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['animal_produccion']
