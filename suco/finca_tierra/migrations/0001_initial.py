# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Acceso'
        db.create_table('finca_tierra_acceso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Acceso'])

        # Adding model 'Parcela'
        db.create_table('finca_tierra_parcela', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Parcela'])

        # Adding model 'Solar'
        db.create_table('finca_tierra_solar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Solar'])

        # Adding model 'Documento'
        db.create_table('finca_tierra_documento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Documento'])

        # Adding model 'AccesoTierra'
        db.create_table('finca_tierra_accesotierra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tierra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.Acceso'])),
            ('parcela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.Parcela'])),
            ('casa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.Solar'])),
            ('documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.Documento'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('finca_tierra', ['AccesoTierra'])

        # Adding model 'Uso'
        db.create_table('finca_tierra_uso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Uso'])

        # Adding model 'UsoTierra'
        db.create_table('finca_tierra_usotierra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tierra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.Uso'])),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('finca_tierra', ['UsoTierra'])

        # Adding model 'AguaAcceso'
        db.create_table('finca_tierra_aguaacceso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['AguaAcceso'])

        # Adding model 'AccesoAgua'
        db.create_table('finca_tierra_accesoagua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.AguaAcceso'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('finca_tierra', ['AccesoAgua'])

        # Adding model 'Maderable'
        db.create_table('finca_tierra_maderable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Maderable'])

        # Adding model 'Forrajero'
        db.create_table('finca_tierra_forrajero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Forrajero'])

        # Adding model 'Energetico'
        db.create_table('finca_tierra_energetico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Energetico'])

        # Adding model 'Frutal'
        db.create_table('finca_tierra_frutal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Frutal'])

        # Adding model 'ExistenciaArboles'
        db.create_table('finca_tierra_existenciaarboles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad_maderable', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_forrajero', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_energetico', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_frutal', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('finca_tierra', ['ExistenciaArboles'])

        # Adding M2M table for field maderable on 'ExistenciaArboles'
        db.create_table('finca_tierra_existenciaarboles_maderable', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['finca_tierra.existenciaarboles'], null=False)),
            ('maderable', models.ForeignKey(orm['finca_tierra.maderable'], null=False))
        ))
        db.create_unique('finca_tierra_existenciaarboles_maderable', ['existenciaarboles_id', 'maderable_id'])

        # Adding M2M table for field forrajero on 'ExistenciaArboles'
        db.create_table('finca_tierra_existenciaarboles_forrajero', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['finca_tierra.existenciaarboles'], null=False)),
            ('forrajero', models.ForeignKey(orm['finca_tierra.forrajero'], null=False))
        ))
        db.create_unique('finca_tierra_existenciaarboles_forrajero', ['existenciaarboles_id', 'forrajero_id'])

        # Adding M2M table for field energetico on 'ExistenciaArboles'
        db.create_table('finca_tierra_existenciaarboles_energetico', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['finca_tierra.existenciaarboles'], null=False)),
            ('energetico', models.ForeignKey(orm['finca_tierra.energetico'], null=False))
        ))
        db.create_unique('finca_tierra_existenciaarboles_energetico', ['existenciaarboles_id', 'energetico_id'])

        # Adding M2M table for field frutal on 'ExistenciaArboles'
        db.create_table('finca_tierra_existenciaarboles_frutal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['finca_tierra.existenciaarboles'], null=False)),
            ('frutal', models.ForeignKey(orm['finca_tierra.frutal'], null=False))
        ))
        db.create_unique('finca_tierra_existenciaarboles_frutal', ['existenciaarboles_id', 'frutal_id'])

        # Adding model 'Actividad'
        db.create_table('finca_tierra_actividad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('finca_tierra', ['Actividad'])

        # Adding model 'Reforestacion'
        db.create_table('finca_tierra_reforestacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reforestacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finca_tierra.Actividad'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('finca_tierra', ['Reforestacion'])


    def backwards(self, orm):
        
        # Deleting model 'Acceso'
        db.delete_table('finca_tierra_acceso')

        # Deleting model 'Parcela'
        db.delete_table('finca_tierra_parcela')

        # Deleting model 'Solar'
        db.delete_table('finca_tierra_solar')

        # Deleting model 'Documento'
        db.delete_table('finca_tierra_documento')

        # Deleting model 'AccesoTierra'
        db.delete_table('finca_tierra_accesotierra')

        # Deleting model 'Uso'
        db.delete_table('finca_tierra_uso')

        # Deleting model 'UsoTierra'
        db.delete_table('finca_tierra_usotierra')

        # Deleting model 'AguaAcceso'
        db.delete_table('finca_tierra_aguaacceso')

        # Deleting model 'AccesoAgua'
        db.delete_table('finca_tierra_accesoagua')

        # Deleting model 'Maderable'
        db.delete_table('finca_tierra_maderable')

        # Deleting model 'Forrajero'
        db.delete_table('finca_tierra_forrajero')

        # Deleting model 'Energetico'
        db.delete_table('finca_tierra_energetico')

        # Deleting model 'Frutal'
        db.delete_table('finca_tierra_frutal')

        # Deleting model 'ExistenciaArboles'
        db.delete_table('finca_tierra_existenciaarboles')

        # Removing M2M table for field maderable on 'ExistenciaArboles'
        db.delete_table('finca_tierra_existenciaarboles_maderable')

        # Removing M2M table for field forrajero on 'ExistenciaArboles'
        db.delete_table('finca_tierra_existenciaarboles_forrajero')

        # Removing M2M table for field energetico on 'ExistenciaArboles'
        db.delete_table('finca_tierra_existenciaarboles_energetico')

        # Removing M2M table for field frutal on 'ExistenciaArboles'
        db.delete_table('finca_tierra_existenciaarboles_frutal')

        # Deleting model 'Actividad'
        db.delete_table('finca_tierra_actividad')

        # Deleting model 'Reforestacion'
        db.delete_table('finca_tierra_reforestacion')


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
        'finca_tierra.acceso': {
            'Meta': {'object_name': 'Acceso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.accesoagua': {
            'Meta': {'object_name': 'AccesoAgua'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.AguaAcceso']"})
        },
        'finca_tierra.accesotierra': {
            'Meta': {'object_name': 'AccesoTierra'},
            'casa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.Solar']"}),
            'documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.Documento']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcela': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.Parcela']"}),
            'tierra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.Acceso']"})
        },
        'finca_tierra.actividad': {
            'Meta': {'object_name': 'Actividad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.aguaacceso': {
            'Meta': {'object_name': 'AguaAcceso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.documento': {
            'Meta': {'object_name': 'Documento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.energetico': {
            'Meta': {'object_name': 'Energetico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.existenciaarboles': {
            'Meta': {'object_name': 'ExistenciaArboles'},
            'cantidad_energetico': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_forrajero': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_frutal': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_maderable': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'energetico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['finca_tierra.Energetico']", 'symmetrical': 'False'}),
            'forrajero': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['finca_tierra.Forrajero']", 'symmetrical': 'False'}),
            'frutal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['finca_tierra.Frutal']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maderable': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['finca_tierra.Maderable']", 'symmetrical': 'False'})
        },
        'finca_tierra.forrajero': {
            'Meta': {'object_name': 'Forrajero'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.frutal': {
            'Meta': {'object_name': 'Frutal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.maderable': {
            'Meta': {'object_name': 'Maderable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.parcela': {
            'Meta': {'object_name': 'Parcela'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.reforestacion': {
            'Meta': {'object_name': 'Reforestacion'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reforestacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.Actividad']"})
        },
        'finca_tierra.solar': {
            'Meta': {'object_name': 'Solar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.uso': {
            'Meta': {'object_name': 'Uso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'finca_tierra.usotierra': {
            'Meta': {'object_name': 'UsoTierra'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tierra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finca_tierra.Uso']"})
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

    complete_apps = ['finca_tierra']
