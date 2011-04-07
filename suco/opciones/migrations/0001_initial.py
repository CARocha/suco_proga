# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ManejoAgro'
        db.create_table('opciones_manejoagro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('opciones', ['ManejoAgro'])

        # Adding model 'OpcionesManejo'
        db.create_table('opciones_opcionesmanejo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.ManejoAgro'])),
            ('nivel', self.gf('django.db.models.fields.IntegerField')()),
            ('menor_escala', self.gf('django.db.models.fields.IntegerField')()),
            ('mayor_escala', self.gf('django.db.models.fields.IntegerField')()),
            ('volumen', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['OpcionesManejo'])

        # Adding model 'Observacion'
        db.create_table('opciones_observacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Observacion'])

        # Adding model 'Sistematica'
        db.create_table('opciones_sistematica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.Observacion'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['Sistematica'])

        # Adding model 'CultivosVariedad'
        db.create_table('opciones_cultivosvariedad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['CultivosVariedad'])

        # Adding model 'Variedades'
        db.create_table('opciones_variedades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.CultivosVariedad'])),
            ('variedad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Variedades'])

        # Adding model 'Semilla'
        db.create_table('opciones_semilla', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cultivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.Variedades'])),
            ('origen', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['Semilla'])

        # Adding model 'Rubros'
        db.create_table('opciones_rubros', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Rubros'])

        # Adding model 'Decision'
        db.create_table('opciones_decision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Decision'])

        # Adding model 'Participasion'
        db.create_table('opciones_participasion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.Rubros'])),
            ('labores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('beneficios', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['Participasion'])

        # Adding M2M table for field decision on 'Participasion'
        db.create_table('opciones_participasion_decision', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participasion', models.ForeignKey(orm['opciones.participasion'], null=False)),
            ('decision', models.ForeignKey(orm['opciones.decision'], null=False))
        ))
        db.create_unique('opciones_participasion_decision', ['participasion_id', 'decision_id'])

        # Adding model 'Textura'
        db.create_table('opciones_textura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Textura'])

        # Adding model 'Profundidad'
        db.create_table('opciones_profundidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Profundidad'])

        # Adding model 'Densidad'
        db.create_table('opciones_densidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Densidad'])

        # Adding model 'Pendiente'
        db.create_table('opciones_pendiente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Pendiente'])

        # Adding model 'Drenaje'
        db.create_table('opciones_drenaje', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Drenaje'])

        # Adding model 'Suelo'
        db.create_table('opciones_suelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['Suelo'])

        # Adding M2M table for field textura on 'Suelo'
        db.create_table('opciones_suelo_textura', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('textura', models.ForeignKey(orm['opciones.textura'], null=False))
        ))
        db.create_unique('opciones_suelo_textura', ['suelo_id', 'textura_id'])

        # Adding M2M table for field profundidad on 'Suelo'
        db.create_table('opciones_suelo_profundidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('profundidad', models.ForeignKey(orm['opciones.profundidad'], null=False))
        ))
        db.create_unique('opciones_suelo_profundidad', ['suelo_id', 'profundidad_id'])

        # Adding M2M table for field lombrices on 'Suelo'
        db.create_table('opciones_suelo_lombrices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['opciones.densidad'], null=False))
        ))
        db.create_unique('opciones_suelo_lombrices', ['suelo_id', 'densidad_id'])

        # Adding M2M table for field densidad on 'Suelo'
        db.create_table('opciones_suelo_densidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['opciones.densidad'], null=False))
        ))
        db.create_unique('opciones_suelo_densidad', ['suelo_id', 'densidad_id'])

        # Adding M2M table for field pendiente on 'Suelo'
        db.create_table('opciones_suelo_pendiente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('pendiente', models.ForeignKey(orm['opciones.pendiente'], null=False))
        ))
        db.create_unique('opciones_suelo_pendiente', ['suelo_id', 'pendiente_id'])

        # Adding M2M table for field drenaje on 'Suelo'
        db.create_table('opciones_suelo_drenaje', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('drenaje', models.ForeignKey(orm['opciones.drenaje'], null=False))
        ))
        db.create_unique('opciones_suelo_drenaje', ['suelo_id', 'drenaje_id'])

        # Adding M2M table for field materia on 'Suelo'
        db.create_table('opciones_suelo_materia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['opciones.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['opciones.densidad'], null=False))
        ))
        db.create_unique('opciones_suelo_materia', ['suelo_id', 'densidad_id'])

        # Adding model 'Preparar'
        db.create_table('opciones_preparar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Preparar'])

        # Adding model 'Traccion'
        db.create_table('opciones_traccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Traccion'])

        # Adding model 'Fertilizacion'
        db.create_table('opciones_fertilizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Fertilizacion'])

        # Adding model 'Conservacion'
        db.create_table('opciones_conservacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Conservacion'])

        # Adding model 'ManejoSuelo'
        db.create_table('opciones_manejosuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analisis', self.gf('django.db.models.fields.IntegerField')()),
            ('practica', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['ManejoSuelo'])

        # Adding M2M table for field preparan on 'ManejoSuelo'
        db.create_table('opciones_manejosuelo_preparan', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['opciones.manejosuelo'], null=False)),
            ('preparar', models.ForeignKey(orm['opciones.preparar'], null=False))
        ))
        db.create_unique('opciones_manejosuelo_preparan', ['manejosuelo_id', 'preparar_id'])

        # Adding M2M table for field traccion on 'ManejoSuelo'
        db.create_table('opciones_manejosuelo_traccion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['opciones.manejosuelo'], null=False)),
            ('traccion', models.ForeignKey(orm['opciones.traccion'], null=False))
        ))
        db.create_unique('opciones_manejosuelo_traccion', ['manejosuelo_id', 'traccion_id'])

        # Adding M2M table for field fertilizacion on 'ManejoSuelo'
        db.create_table('opciones_manejosuelo_fertilizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['opciones.manejosuelo'], null=False)),
            ('fertilizacion', models.ForeignKey(orm['opciones.fertilizacion'], null=False))
        ))
        db.create_unique('opciones_manejosuelo_fertilizacion', ['manejosuelo_id', 'fertilizacion_id'])

        # Adding M2M table for field obra on 'ManejoSuelo'
        db.create_table('opciones_manejosuelo_obra', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['opciones.manejosuelo'], null=False)),
            ('conservacion', models.ForeignKey(orm['opciones.conservacion'], null=False))
        ))
        db.create_unique('opciones_manejosuelo_obra', ['manejosuelo_id', 'conservacion_id'])

        # Adding model 'Procesado'
        db.create_table('opciones_procesado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Procesado'])

        # Adding model 'Procesamiento'
        db.create_table('opciones_procesamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.Procesado'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('aditivos', self.gf('django.db.models.fields.IntegerField')()),
            ('empaque', self.gf('django.db.models.fields.IntegerField')()),
            ('comercializada', self.gf('django.db.models.fields.FloatField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['Procesamiento'])

        # Adding model 'Fuente'
        db.create_table('opciones_fuente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['Fuente'])

        # Adding model 'TipoTrabajo'
        db.create_table('opciones_tipotrabajo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fuente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.Fuente'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('opciones', ['TipoTrabajo'])

        # Adding model 'OtrosIngresos'
        db.create_table('opciones_otrosingresos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trabajo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opciones.TipoTrabajo'])),
            ('meses', self.gf('django.db.models.fields.IntegerField')()),
            ('Ingreso', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('tiene_ingreso', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('opciones', ['OtrosIngresos'])


    def backwards(self, orm):
        
        # Deleting model 'ManejoAgro'
        db.delete_table('opciones_manejoagro')

        # Deleting model 'OpcionesManejo'
        db.delete_table('opciones_opcionesmanejo')

        # Deleting model 'Observacion'
        db.delete_table('opciones_observacion')

        # Deleting model 'Sistematica'
        db.delete_table('opciones_sistematica')

        # Deleting model 'CultivosVariedad'
        db.delete_table('opciones_cultivosvariedad')

        # Deleting model 'Variedades'
        db.delete_table('opciones_variedades')

        # Deleting model 'Semilla'
        db.delete_table('opciones_semilla')

        # Deleting model 'Rubros'
        db.delete_table('opciones_rubros')

        # Deleting model 'Decision'
        db.delete_table('opciones_decision')

        # Deleting model 'Participasion'
        db.delete_table('opciones_participasion')

        # Removing M2M table for field decision on 'Participasion'
        db.delete_table('opciones_participasion_decision')

        # Deleting model 'Textura'
        db.delete_table('opciones_textura')

        # Deleting model 'Profundidad'
        db.delete_table('opciones_profundidad')

        # Deleting model 'Densidad'
        db.delete_table('opciones_densidad')

        # Deleting model 'Pendiente'
        db.delete_table('opciones_pendiente')

        # Deleting model 'Drenaje'
        db.delete_table('opciones_drenaje')

        # Deleting model 'Suelo'
        db.delete_table('opciones_suelo')

        # Removing M2M table for field textura on 'Suelo'
        db.delete_table('opciones_suelo_textura')

        # Removing M2M table for field profundidad on 'Suelo'
        db.delete_table('opciones_suelo_profundidad')

        # Removing M2M table for field lombrices on 'Suelo'
        db.delete_table('opciones_suelo_lombrices')

        # Removing M2M table for field densidad on 'Suelo'
        db.delete_table('opciones_suelo_densidad')

        # Removing M2M table for field pendiente on 'Suelo'
        db.delete_table('opciones_suelo_pendiente')

        # Removing M2M table for field drenaje on 'Suelo'
        db.delete_table('opciones_suelo_drenaje')

        # Removing M2M table for field materia on 'Suelo'
        db.delete_table('opciones_suelo_materia')

        # Deleting model 'Preparar'
        db.delete_table('opciones_preparar')

        # Deleting model 'Traccion'
        db.delete_table('opciones_traccion')

        # Deleting model 'Fertilizacion'
        db.delete_table('opciones_fertilizacion')

        # Deleting model 'Conservacion'
        db.delete_table('opciones_conservacion')

        # Deleting model 'ManejoSuelo'
        db.delete_table('opciones_manejosuelo')

        # Removing M2M table for field preparan on 'ManejoSuelo'
        db.delete_table('opciones_manejosuelo_preparan')

        # Removing M2M table for field traccion on 'ManejoSuelo'
        db.delete_table('opciones_manejosuelo_traccion')

        # Removing M2M table for field fertilizacion on 'ManejoSuelo'
        db.delete_table('opciones_manejosuelo_fertilizacion')

        # Removing M2M table for field obra on 'ManejoSuelo'
        db.delete_table('opciones_manejosuelo_obra')

        # Deleting model 'Procesado'
        db.delete_table('opciones_procesado')

        # Deleting model 'Procesamiento'
        db.delete_table('opciones_procesamiento')

        # Deleting model 'Fuente'
        db.delete_table('opciones_fuente')

        # Deleting model 'TipoTrabajo'
        db.delete_table('opciones_tipotrabajo')

        # Deleting model 'OtrosIngresos'
        db.delete_table('opciones_otrosingresos')


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
            'beneficios': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'decision': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opciones.Decision']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opciones.Observacion']"})
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
