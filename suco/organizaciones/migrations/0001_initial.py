# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OrgGremiales'
        db.create_table('organizaciones_orggremiales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizaciones', ['OrgGremiales'])

        # Adding model 'OrganizacionGremial'
        db.create_table('organizaciones_organizaciongremial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desde_socio', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('organizaciones', ['OrganizacionGremial'])

        # Adding M2M table for field socio on 'OrganizacionGremial'
        db.create_table('organizaciones_organizaciongremial_socio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm['organizaciones.organizaciongremial'], null=False)),
            ('orggremiales', models.ForeignKey(orm['organizaciones.orggremiales'], null=False))
        ))
        db.create_unique('organizaciones_organizaciongremial_socio', ['organizaciongremial_id', 'orggremiales_id'])

        # Adding model 'OrgComunitarias'
        db.create_table('organizaciones_orgcomunitarias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizaciones', ['OrgComunitarias'])

        # Adding model 'BeneficioOrgComunitaria'
        db.create_table('organizaciones_beneficioorgcomunitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizaciones', ['BeneficioOrgComunitaria'])

        # Adding model 'NoOrganizado'
        db.create_table('organizaciones_noorganizado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizaciones', ['NoOrganizado'])

        # Adding model 'OrganizacionComunitaria'
        db.create_table('organizaciones_organizacioncomunitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('pertence', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
        ))
        db.send_create_signal('organizaciones', ['OrganizacionComunitaria'])

        # Adding M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.create_table('organizaciones_organizacioncomunitaria_cual_organizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['organizaciones.organizacioncomunitaria'], null=False)),
            ('orgcomunitarias', models.ForeignKey(orm['organizaciones.orgcomunitarias'], null=False))
        ))
        db.create_unique('organizaciones_organizacioncomunitaria_cual_organizacion', ['organizacioncomunitaria_id', 'orgcomunitarias_id'])

        # Adding M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.create_table('organizaciones_organizacioncomunitaria_cual_beneficio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['organizaciones.organizacioncomunitaria'], null=False)),
            ('beneficioorgcomunitaria', models.ForeignKey(orm['organizaciones.beneficioorgcomunitaria'], null=False))
        ))
        db.create_unique('organizaciones_organizacioncomunitaria_cual_beneficio', ['organizacioncomunitaria_id', 'beneficioorgcomunitaria_id'])

        # Adding M2M table for field no_organizado on 'OrganizacionComunitaria'
        db.create_table('organizaciones_organizacioncomunitaria_no_organizado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['organizaciones.organizacioncomunitaria'], null=False)),
            ('noorganizado', models.ForeignKey(orm['organizaciones.noorganizado'], null=False))
        ))
        db.create_unique('organizaciones_organizacioncomunitaria_no_organizado', ['organizacioncomunitaria_id', 'noorganizado_id'])


    def backwards(self, orm):
        
        # Deleting model 'OrgGremiales'
        db.delete_table('organizaciones_orggremiales')

        # Deleting model 'OrganizacionGremial'
        db.delete_table('organizaciones_organizaciongremial')

        # Removing M2M table for field socio on 'OrganizacionGremial'
        db.delete_table('organizaciones_organizaciongremial_socio')

        # Deleting model 'OrgComunitarias'
        db.delete_table('organizaciones_orgcomunitarias')

        # Deleting model 'BeneficioOrgComunitaria'
        db.delete_table('organizaciones_beneficioorgcomunitaria')

        # Deleting model 'NoOrganizado'
        db.delete_table('organizaciones_noorganizado')

        # Deleting model 'OrganizacionComunitaria'
        db.delete_table('organizaciones_organizacioncomunitaria')

        # Removing M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.delete_table('organizaciones_organizacioncomunitaria_cual_organizacion')

        # Removing M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.delete_table('organizaciones_organizacioncomunitaria_cual_beneficio')

        # Removing M2M table for field no_organizado on 'OrganizacionComunitaria'
        db.delete_table('organizaciones_organizacioncomunitaria_no_organizado')


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
        'organizaciones.beneficioorgcomunitaria': {
            'Meta': {'object_name': 'BeneficioOrgComunitaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizaciones.noorganizado': {
            'Meta': {'object_name': 'NoOrganizado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizaciones.organizacioncomunitaria': {
            'Meta': {'object_name': 'OrganizacionComunitaria'},
            'cual_beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['organizaciones.BeneficioOrgComunitaria']", 'symmetrical': 'False'}),
            'cual_organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['organizaciones.OrgComunitarias']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['organizaciones.NoOrganizado']", 'symmetrical': 'False'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'pertence': ('django.db.models.fields.IntegerField', [], {})
        },
        'organizaciones.organizaciongremial': {
            'Meta': {'object_name': 'OrganizacionGremial'},
            'desde_socio': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['organizaciones.OrgGremiales']", 'symmetrical': 'False'})
        },
        'organizaciones.orgcomunitarias': {
            'Meta': {'object_name': 'OrgComunitarias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizaciones.orggremiales': {
            'Meta': {'object_name': 'OrgGremiales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['organizaciones']
