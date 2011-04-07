# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Educacion'
        db.create_table('familias_educacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('no_leer', self.gf('django.db.models.fields.IntegerField')()),
            ('p_incompleta', self.gf('django.db.models.fields.IntegerField')()),
            ('p_completa', self.gf('django.db.models.fields.IntegerField')()),
            ('s_incompleta', self.gf('django.db.models.fields.IntegerField')()),
            ('bachiller', self.gf('django.db.models.fields.IntegerField')()),
            ('universitario', self.gf('django.db.models.fields.IntegerField')()),
            ('f_comunidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Educacion'])

        # Adding model 'Salud'
        db.create_table('familias_salud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('b_salud', self.gf('django.db.models.fields.IntegerField')()),
            ('s_delicada', self.gf('django.db.models.fields.IntegerField')()),
            ('e_cronica', self.gf('django.db.models.fields.IntegerField')()),
            ('v_centro', self.gf('django.db.models.fields.IntegerField')()),
            ('v_medico', self.gf('django.db.models.fields.IntegerField')()),
            ('v_naturista', self.gf('django.db.models.fields.IntegerField')()),
            ('automedica', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Salud'])

        # Adding model 'PreguntaEnergia'
        db.create_table('familias_preguntaenergia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['PreguntaEnergia'])

        # Adding model 'Cocinar'
        db.create_table('familias_cocinar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['Cocinar'])

        # Adding model 'Energia'
        db.create_table('familias_energia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['familias.PreguntaEnergia'])),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Energia'])

        # Adding model 'QueUtiliza'
        db.create_table('familias_queutiliza', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('familias', ['QueUtiliza'])

        # Adding M2M table for field cocina on 'QueUtiliza'
        db.create_table('familias_queutiliza_cocina', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('queutiliza', models.ForeignKey(orm['familias.queutiliza'], null=False)),
            ('cocinar', models.ForeignKey(orm['familias.cocinar'], null=False))
        ))
        db.create_unique('familias_queutiliza_cocina', ['queutiliza_id', 'cocinar_id'])

        # Adding model 'FuenteConsumo'
        db.create_table('familias_fuenteconsumo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['FuenteConsumo'])

        # Adding model 'TrataAgua'
        db.create_table('familias_trataagua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['TrataAgua'])

        # Adding model 'DisponibilidadAgua'
        db.create_table('familias_disponibilidadagua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['DisponibilidadAgua'])

        # Adding model 'AguaConsumo'
        db.create_table('familias_aguaconsumo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('familias', ['AguaConsumo'])

        # Adding M2M table for field fuente on 'AguaConsumo'
        db.create_table('familias_aguaconsumo_fuente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aguaconsumo', models.ForeignKey(orm['familias.aguaconsumo'], null=False)),
            ('fuenteconsumo', models.ForeignKey(orm['familias.fuenteconsumo'], null=False))
        ))
        db.create_unique('familias_aguaconsumo_fuente', ['aguaconsumo_id', 'fuenteconsumo_id'])

        # Adding M2M table for field tratar on 'AguaConsumo'
        db.create_table('familias_aguaconsumo_tratar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aguaconsumo', models.ForeignKey(orm['familias.aguaconsumo'], null=False)),
            ('trataagua', models.ForeignKey(orm['familias.trataagua'], null=False))
        ))
        db.create_unique('familias_aguaconsumo_tratar', ['aguaconsumo_id', 'trataagua_id'])

        # Adding M2M table for field disponible on 'AguaConsumo'
        db.create_table('familias_aguaconsumo_disponible', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aguaconsumo', models.ForeignKey(orm['familias.aguaconsumo'], null=False)),
            ('disponibilidadagua', models.ForeignKey(orm['familias.disponibilidadagua'], null=False))
        ))
        db.create_unique('familias_aguaconsumo_disponible', ['aguaconsumo_id', 'disponibilidadagua_id'])

        # Adding model 'FuenteProduccion'
        db.create_table('familias_fuenteproduccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['FuenteProduccion'])

        # Adding model 'EquipoBombeo'
        db.create_table('familias_equipobombeo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['EquipoBombeo'])

        # Adding model 'EnergiaUtiliza'
        db.create_table('familias_energiautiliza', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['EnergiaUtiliza'])

        # Adding model 'AguaProduccion'
        db.create_table('familias_aguaproduccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('familias', ['AguaProduccion'])

        # Adding M2M table for field fuente on 'AguaProduccion'
        db.create_table('familias_aguaproduccion_fuente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aguaproduccion', models.ForeignKey(orm['familias.aguaproduccion'], null=False)),
            ('fuenteproduccion', models.ForeignKey(orm['familias.fuenteproduccion'], null=False))
        ))
        db.create_unique('familias_aguaproduccion_fuente', ['aguaproduccion_id', 'fuenteproduccion_id'])

        # Adding M2M table for field equipo on 'AguaProduccion'
        db.create_table('familias_aguaproduccion_equipo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aguaproduccion', models.ForeignKey(orm['familias.aguaproduccion'], null=False)),
            ('equipobombeo', models.ForeignKey(orm['familias.equipobombeo'], null=False))
        ))
        db.create_unique('familias_aguaproduccion_equipo', ['aguaproduccion_id', 'equipobombeo_id'])

        # Adding M2M table for field energia on 'AguaProduccion'
        db.create_table('familias_aguaproduccion_energia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aguaproduccion', models.ForeignKey(orm['familias.aguaproduccion'], null=False)),
            ('energiautiliza', models.ForeignKey(orm['familias.energiautiliza'], null=False))
        ))
        db.create_unique('familias_aguaproduccion_energia', ['aguaproduccion_id', 'energiautiliza_id'])


    def backwards(self, orm):
        
        # Deleting model 'Educacion'
        db.delete_table('familias_educacion')

        # Deleting model 'Salud'
        db.delete_table('familias_salud')

        # Deleting model 'PreguntaEnergia'
        db.delete_table('familias_preguntaenergia')

        # Deleting model 'Cocinar'
        db.delete_table('familias_cocinar')

        # Deleting model 'Energia'
        db.delete_table('familias_energia')

        # Deleting model 'QueUtiliza'
        db.delete_table('familias_queutiliza')

        # Removing M2M table for field cocina on 'QueUtiliza'
        db.delete_table('familias_queutiliza_cocina')

        # Deleting model 'FuenteConsumo'
        db.delete_table('familias_fuenteconsumo')

        # Deleting model 'TrataAgua'
        db.delete_table('familias_trataagua')

        # Deleting model 'DisponibilidadAgua'
        db.delete_table('familias_disponibilidadagua')

        # Deleting model 'AguaConsumo'
        db.delete_table('familias_aguaconsumo')

        # Removing M2M table for field fuente on 'AguaConsumo'
        db.delete_table('familias_aguaconsumo_fuente')

        # Removing M2M table for field tratar on 'AguaConsumo'
        db.delete_table('familias_aguaconsumo_tratar')

        # Removing M2M table for field disponible on 'AguaConsumo'
        db.delete_table('familias_aguaconsumo_disponible')

        # Deleting model 'FuenteProduccion'
        db.delete_table('familias_fuenteproduccion')

        # Deleting model 'EquipoBombeo'
        db.delete_table('familias_equipobombeo')

        # Deleting model 'EnergiaUtiliza'
        db.delete_table('familias_energiautiliza')

        # Deleting model 'AguaProduccion'
        db.delete_table('familias_aguaproduccion')

        # Removing M2M table for field fuente on 'AguaProduccion'
        db.delete_table('familias_aguaproduccion_fuente')

        # Removing M2M table for field equipo on 'AguaProduccion'
        db.delete_table('familias_aguaproduccion_equipo')

        # Removing M2M table for field energia on 'AguaProduccion'
        db.delete_table('familias_aguaproduccion_energia')


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
        'familias.aguaconsumo': {
            'Meta': {'object_name': 'AguaConsumo'},
            'disponible': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.DisponibilidadAgua']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.FuenteConsumo']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tratar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.TrataAgua']", 'symmetrical': 'False'})
        },
        'familias.aguaproduccion': {
            'Meta': {'object_name': 'AguaProduccion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'energia': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.EnergiaUtiliza']", 'symmetrical': 'False'}),
            'equipo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.EquipoBombeo']", 'symmetrical': 'False'}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.FuenteProduccion']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'familias.cocinar': {
            'Meta': {'object_name': 'Cocinar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.disponibilidadagua': {
            'Meta': {'object_name': 'DisponibilidadAgua'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.educacion': {
            'Meta': {'object_name': 'Educacion'},
            'bachiller': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'f_comunidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_leer': ('django.db.models.fields.IntegerField', [], {}),
            'p_completa': ('django.db.models.fields.IntegerField', [], {}),
            'p_incompleta': ('django.db.models.fields.IntegerField', [], {}),
            's_incompleta': ('django.db.models.fields.IntegerField', [], {}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'universitario': ('django.db.models.fields.IntegerField', [], {})
        },
        'familias.energia': {
            'Meta': {'object_name': 'Energia'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['familias.PreguntaEnergia']"}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'familias.energiautiliza': {
            'Meta': {'object_name': 'EnergiaUtiliza'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.equipobombeo': {
            'Meta': {'object_name': 'EquipoBombeo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.fuenteconsumo': {
            'Meta': {'object_name': 'FuenteConsumo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.fuenteproduccion': {
            'Meta': {'object_name': 'FuenteProduccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.preguntaenergia': {
            'Meta': {'object_name': 'PreguntaEnergia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.queutiliza': {
            'Meta': {'object_name': 'QueUtiliza'},
            'cocina': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['familias.Cocinar']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'familias.salud': {
            'Meta': {'object_name': 'Salud'},
            'automedica': ('django.db.models.fields.IntegerField', [], {}),
            'b_salud': ('django.db.models.fields.IntegerField', [], {}),
            'e_cronica': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            's_delicada': ('django.db.models.fields.IntegerField', [], {}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'v_centro': ('django.db.models.fields.IntegerField', [], {}),
            'v_medico': ('django.db.models.fields.IntegerField', [], {}),
            'v_naturista': ('django.db.models.fields.IntegerField', [], {})
        },
        'familias.trataagua': {
            'Meta': {'object_name': 'TrataAgua'},
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

    complete_apps = ['familias']
