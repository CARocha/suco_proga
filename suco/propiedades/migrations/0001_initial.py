# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Piso'
        db.create_table('propiedades_piso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['Piso'])

        # Adding model 'Techo'
        db.create_table('propiedades_techo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['Techo'])

        # Adding model 'TipoCasa'
        db.create_table('propiedades_tipocasa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['TipoCasa'])

        # Adding M2M table for field piso on 'TipoCasa'
        db.create_table('propiedades_tipocasa_piso', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['propiedades.tipocasa'], null=False)),
            ('piso', models.ForeignKey(orm['propiedades.piso'], null=False))
        ))
        db.create_unique('propiedades_tipocasa_piso', ['tipocasa_id', 'piso_id'])

        # Adding M2M table for field techo on 'TipoCasa'
        db.create_table('propiedades_tipocasa_techo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['propiedades.tipocasa'], null=False)),
            ('techo', models.ForeignKey(orm['propiedades.techo'], null=False))
        ))
        db.create_unique('propiedades_tipocasa_techo', ['tipocasa_id', 'techo_id'])

        # Adding model 'DetalleCasa'
        db.create_table('propiedades_detallecasa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tamano', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ambientes', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('letrina', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lavadero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['DetalleCasa'])

        # Adding model 'Equipos'
        db.create_table('propiedades_equipos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['Equipos'])

        # Adding model 'Infraestructuras'
        db.create_table('propiedades_infraestructuras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['Infraestructuras'])

        # Adding model 'Electro'
        db.create_table('propiedades_electro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['Electro'])

        # Adding model 'Sanamiento'
        db.create_table('propiedades_sanamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['Sanamiento'])

        # Adding model 'PropiedadEquipo'
        db.create_table('propiedades_propiedadequipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.Equipos'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['PropiedadEquipo'])

        # Adding model 'PropiedadInfra'
        db.create_table('propiedades_propiedadinfra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('infraestructura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.Infraestructuras'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['PropiedadInfra'])

        # Adding model 'Electrodomestico'
        db.create_table('propiedades_electrodomestico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('electro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.Electro'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['Electrodomestico'])

        # Adding model 'Sana'
        db.create_table('propiedades_sana', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('electro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.Sanamiento'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['Sana'])

        # Adding model 'NombreHerramienta'
        db.create_table('propiedades_nombreherramienta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['NombreHerramienta'])

        # Adding model 'Herramientas'
        db.create_table('propiedades_herramientas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramienta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.NombreHerramienta'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['Herramientas'])

        # Adding model 'NombreTransporte'
        db.create_table('propiedades_nombretransporte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['NombreTransporte'])

        # Adding model 'Transporte'
        db.create_table('propiedades_transporte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.NombreTransporte'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['Transporte'])

        # Adding model 'AhorroPregunta'
        db.create_table('propiedades_ahorropregunta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('propiedades', ['AhorroPregunta'])

        # Adding model 'Ahorro'
        db.create_table('propiedades_ahorro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ahorro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['propiedades.AhorroPregunta'])),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['Ahorro'])

        # Adding model 'DaCredito'
        db.create_table('propiedades_dacredito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['DaCredito'])

        # Adding model 'OcupaCredito'
        db.create_table('propiedades_ocupacredito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('propiedades', ['OcupaCredito'])

        # Adding model 'Credito'
        db.create_table('propiedades_credito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recibe', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('desde', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('satisfaccion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('propiedades', ['Credito'])

        # Adding M2M table for field quien_credito on 'Credito'
        db.create_table('propiedades_credito_quien_credito', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('credito', models.ForeignKey(orm['propiedades.credito'], null=False)),
            ('dacredito', models.ForeignKey(orm['propiedades.dacredito'], null=False))
        ))
        db.create_unique('propiedades_credito_quien_credito', ['credito_id', 'dacredito_id'])

        # Adding M2M table for field ocupa_credito on 'Credito'
        db.create_table('propiedades_credito_ocupa_credito', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('credito', models.ForeignKey(orm['propiedades.credito'], null=False)),
            ('ocupacredito', models.ForeignKey(orm['propiedades.ocupacredito'], null=False))
        ))
        db.create_unique('propiedades_credito_ocupa_credito', ['credito_id', 'ocupacredito_id'])


    def backwards(self, orm):
        
        # Deleting model 'Piso'
        db.delete_table('propiedades_piso')

        # Deleting model 'Techo'
        db.delete_table('propiedades_techo')

        # Deleting model 'TipoCasa'
        db.delete_table('propiedades_tipocasa')

        # Removing M2M table for field piso on 'TipoCasa'
        db.delete_table('propiedades_tipocasa_piso')

        # Removing M2M table for field techo on 'TipoCasa'
        db.delete_table('propiedades_tipocasa_techo')

        # Deleting model 'DetalleCasa'
        db.delete_table('propiedades_detallecasa')

        # Deleting model 'Equipos'
        db.delete_table('propiedades_equipos')

        # Deleting model 'Infraestructuras'
        db.delete_table('propiedades_infraestructuras')

        # Deleting model 'Electro'
        db.delete_table('propiedades_electro')

        # Deleting model 'Sanamiento'
        db.delete_table('propiedades_sanamiento')

        # Deleting model 'PropiedadEquipo'
        db.delete_table('propiedades_propiedadequipo')

        # Deleting model 'PropiedadInfra'
        db.delete_table('propiedades_propiedadinfra')

        # Deleting model 'Electrodomestico'
        db.delete_table('propiedades_electrodomestico')

        # Deleting model 'Sana'
        db.delete_table('propiedades_sana')

        # Deleting model 'NombreHerramienta'
        db.delete_table('propiedades_nombreherramienta')

        # Deleting model 'Herramientas'
        db.delete_table('propiedades_herramientas')

        # Deleting model 'NombreTransporte'
        db.delete_table('propiedades_nombretransporte')

        # Deleting model 'Transporte'
        db.delete_table('propiedades_transporte')

        # Deleting model 'AhorroPregunta'
        db.delete_table('propiedades_ahorropregunta')

        # Deleting model 'Ahorro'
        db.delete_table('propiedades_ahorro')

        # Deleting model 'DaCredito'
        db.delete_table('propiedades_dacredito')

        # Deleting model 'OcupaCredito'
        db.delete_table('propiedades_ocupacredito')

        # Deleting model 'Credito'
        db.delete_table('propiedades_credito')

        # Removing M2M table for field quien_credito on 'Credito'
        db.delete_table('propiedades_credito_quien_credito')

        # Removing M2M table for field ocupa_credito on 'Credito'
        db.delete_table('propiedades_credito_ocupa_credito')


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
        'propiedades.ahorro': {
            'Meta': {'object_name': 'Ahorro'},
            'ahorro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.AhorroPregunta']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'propiedades.ahorropregunta': {
            'Meta': {'object_name': 'AhorroPregunta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'propiedades.credito': {
            'Meta': {'object_name': 'Credito'},
            'desde': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ocupa_credito': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['propiedades.OcupaCredito']", 'null': 'True', 'blank': 'True'}),
            'quien_credito': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['propiedades.DaCredito']", 'null': 'True', 'blank': 'True'}),
            'recibe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'satisfaccion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'propiedades.dacredito': {
            'Meta': {'object_name': 'DaCredito'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.detallecasa': {
            'Meta': {'object_name': 'DetalleCasa'},
            'ambientes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lavadero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'letrina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tamano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'propiedades.electro': {
            'Meta': {'object_name': 'Electro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.electrodomestico': {
            'Meta': {'object_name': 'Electrodomestico'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'electro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.Electro']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'propiedades.equipos': {
            'Meta': {'object_name': 'Equipos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.herramientas': {
            'Meta': {'object_name': 'Herramientas'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'herramienta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.NombreHerramienta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        'propiedades.infraestructuras': {
            'Meta': {'object_name': 'Infraestructuras'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.nombreherramienta': {
            'Meta': {'object_name': 'NombreHerramienta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.nombretransporte': {
            'Meta': {'object_name': 'NombreTransporte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.ocupacredito': {
            'Meta': {'object_name': 'OcupaCredito'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.piso': {
            'Meta': {'object_name': 'Piso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.propiedadequipo': {
            'Meta': {'object_name': 'PropiedadEquipo'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.Equipos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'propiedades.propiedadinfra': {
            'Meta': {'object_name': 'PropiedadInfra'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.Infraestructuras']"})
        },
        'propiedades.sana': {
            'Meta': {'object_name': 'Sana'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'electro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.Sanamiento']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'propiedades.sanamiento': {
            'Meta': {'object_name': 'Sanamiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.techo': {
            'Meta': {'object_name': 'Techo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'propiedades.tipocasa': {
            'Meta': {'object_name': 'TipoCasa'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piso': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['propiedades.Piso']", 'symmetrical': 'False'}),
            'techo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['propiedades.Techo']", 'symmetrical': 'False'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'propiedades.transporte': {
            'Meta': {'object_name': 'Transporte'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'transporte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['propiedades.NombreTransporte']"})
        }
    }

    complete_apps = ['propiedades']
