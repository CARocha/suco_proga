# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Participasion.labores'
        db.delete_column('opciones_participasion', 'labores')

        # Deleting field 'Participasion.beneficios'
        db.delete_column('opciones_participasion', 'beneficios')

        # Adding M2M table for field labores on 'Participasion'
        db.create_table('opciones_participasion_labores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participasion', models.ForeignKey(orm['opciones.participasion'], null=False)),
            ('decision', models.ForeignKey(orm['opciones.decision'], null=False))
        ))
        db.create_unique('opciones_participasion_labores', ['participasion_id', 'decision_id'])

        # Adding M2M table for field beneficios on 'Participasion'
        db.create_table('opciones_participasion_beneficios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participasion', models.ForeignKey(orm['opciones.participasion'], null=False)),
            ('decision', models.ForeignKey(orm['opciones.decision'], null=False))
        ))
        db.create_unique('opciones_participasion_beneficios', ['participasion_id', 'decision_id'])


    def backwards(self, orm):
        
        # Adding field 'Participasion.labores'
        db.add_column('opciones_participasion', 'labores', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Participasion.beneficios'
        db.add_column('opciones_participasion', 'beneficios', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Removing M2M table for field labores on 'Participasion'
        db.delete_table('opciones_participasion_labores')

        # Removing M2M table for field beneficios on 'Participasion'
        db.delete_table('opciones_participasion_beneficios')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('suco.smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'escolaridad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Escolaridad']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'formacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Tecnica']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'participacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ParticipacionProyecto']", 'symmetrical': 'False'}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
        'opciones.conservacion': {
            'Meta': {'object_name': 'Conservacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.cultivosvariedad': {
            'Meta': {'object_name': 'CultivosVariedad'},
            'cultivo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'opciones.decision': {
            'Meta': {'object_name': 'Decision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.densidad': {
            'Meta': {'object_name': 'Densidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.drenaje': {
            'Meta': {'object_name': 'Drenaje'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.fertilizacion': {
            'Meta': {'object_name': 'Fertilizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.fuente': {
            'Meta': {'object_name': 'Fuente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.manejoagro': {
            'Meta': {'object_name': 'ManejoAgro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'opciones.manejosuelo': {
            'Meta': {'object_name': 'ManejoSuelo'},
            'analisis': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'fertilizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Fertilizacion']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Conservacion']", 'symmetrical': 'False'}),
            'practica': ('django.db.models.fields.IntegerField', [], {}),
            'preparan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Preparar']", 'symmetrical': 'False'}),
            'traccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Traccion']", 'symmetrical': 'False'})
        },
        'opciones.observacion': {
            'Meta': {'object_name': 'Observacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.opcionesmanejo': {
            'Meta': {'object_name': 'OpcionesManejo'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mayor_escala': ('django.db.models.fields.IntegerField', [], {}),
            'menor_escala': ('django.db.models.fields.IntegerField', [], {}),
            'nivel': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.ManejoAgro']"}),
            'volumen': ('django.db.models.fields.FloatField', [], {})
        },
        'opciones.otrosingresos': {
            'Ingreso': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'OtrosIngresos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('django.db.models.fields.IntegerField', [], {}),
            'tiene_ingreso': ('django.db.models.fields.IntegerField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'trabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.TipoTrabajo']"})
        },
        'opciones.participasion': {
            'Meta': {'object_name': 'Participasion'},
            'beneficios': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'beneficio'", 'symmetrical': 'False', 'to': "orm['opciones.Decision']"}),
            'decision': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'decision'", 'symmetrical': 'False', 'to': "orm['opciones.Decision']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'labore'", 'symmetrical': 'False', 'to': "orm['opciones.Decision']"}),
            'rubro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.Rubros']"})
        },
        'opciones.pendiente': {
            'Meta': {'object_name': 'Pendiente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.preparar': {
            'Meta': {'object_name': 'Preparar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.procesado': {
            'Meta': {'object_name': 'Procesado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.procesamiento': {
            'Meta': {'object_name': 'Procesamiento'},
            'aditivos': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'comercializada': ('django.db.models.fields.FloatField', [], {}),
            'empaque': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.Procesado']"})
        },
        'opciones.profundidad': {
            'Meta': {'object_name': 'Profundidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.rubros': {
            'Meta': {'object_name': 'Rubros'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.semilla': {
            'Meta': {'object_name': 'Semilla'},
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.Variedades']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origen': ('django.db.models.fields.IntegerField', [], {})
        },
        'opciones.sistematica': {
            'Meta': {'object_name': 'Sistematica'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['opciones.Observacion']", 'null': 'True', 'blank': 'True'})
        },
        'opciones.suelo': {
            'Meta': {'object_name': 'Suelo'},
            'densidad': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'densidad'", 'symmetrical': 'False', 'to': "orm['opciones.Densidad']"}),
            'drenaje': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Drenaje']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lombrices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lombrices'", 'symmetrical': 'False', 'to': "orm['opciones.Densidad']"}),
            'materia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'materia'", 'symmetrical': 'False', 'to': "orm['opciones.Densidad']"}),
            'pendiente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Pendiente']", 'symmetrical': 'False'}),
            'profundidad': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Profundidad']", 'symmetrical': 'False'}),
            'textura': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Textura']", 'symmetrical': 'False'})
        },
        'opciones.textura': {
            'Meta': {'object_name': 'Textura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.tipotrabajo': {
            'Meta': {'object_name': 'TipoTrabajo'},
            'fuente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.Fuente']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.traccion': {
            'Meta': {'object_name': 'Traccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'opciones.variedades': {
            'Meta': {'object_name': 'Variedades'},
            'cultivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.CultivosVariedad']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'variedad': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['opciones']
