# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table(u'feed_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_app.CustomUser'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'feed', ['Entry'])

        # Adding model 'TextEntry'
        db.create_table(u'feed_textentry', (
            (u'entry_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feed.Entry'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'feed', ['TextEntry'])

        # Adding model 'PictureEntry'
        db.create_table(u'feed_pictureentry', (
            (u'entry_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feed.Entry'], unique=True, primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'feed', ['PictureEntry'])

        # Adding model 'VideoEntry'
        db.create_table(u'feed_videoentry', (
            (u'entry_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feed.Entry'], unique=True, primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'feed', ['VideoEntry'])

        # Adding model 'EventEntry'
        db.create_table(u'feed_evententry', (
            (u'entry_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feed.Entry'], unique=True, primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'feed', ['EventEntry'])

        # Adding model 'BlogEntry'
        db.create_table(u'feed_blogentry', (
            (u'entry_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feed.Entry'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'feed', ['BlogEntry'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table(u'feed_entry')

        # Deleting model 'TextEntry'
        db.delete_table(u'feed_textentry')

        # Deleting model 'PictureEntry'
        db.delete_table(u'feed_pictureentry')

        # Deleting model 'VideoEntry'
        db.delete_table(u'feed_videoentry')

        # Deleting model 'EventEntry'
        db.delete_table(u'feed_evententry')

        # Deleting model 'BlogEntry'
        db.delete_table(u'feed_blogentry')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feed.blogentry': {
            'Meta': {'object_name': 'BlogEntry', '_ormbases': [u'feed.Entry']},
            u'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feed.Entry']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'feed.entry': {
            'Meta': {'object_name': 'Entry'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_app.CustomUser']"})
        },
        u'feed.evententry': {
            'Meta': {'object_name': 'EventEntry', '_ormbases': [u'feed.Entry']},
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feed.Entry']", 'unique': 'True', 'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'feed.pictureentry': {
            'Meta': {'object_name': 'PictureEntry', '_ormbases': [u'feed.Entry']},
            u'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feed.Entry']", 'unique': 'True', 'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'feed.textentry': {
            'Meta': {'object_name': 'TextEntry', '_ormbases': [u'feed.Entry']},
            u'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feed.Entry']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'feed.videoentry': {
            'Meta': {'object_name': 'VideoEntry', '_ormbases': [u'feed.Entry']},
            u'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feed.Entry']", 'unique': 'True', 'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'user_app.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'corporation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'US'", 'max_length': '100', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'postal_box': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_line1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'user_app.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'blank': 'True'}),
            'chargify_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'connection': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_connections'", 'null': 'True', 'to': u"orm['user_app.Professional']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'default': "'default-profile.svg'", 'max_length': '100', 'blank': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_professional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_upgraded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'default': "'29.760193'", 'max_length': '30', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'default': "'-95.369390'", 'max_length': '30', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'plus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'primary_address': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'owner'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['user_app.Address']", 'blank': 'True', 'unique': 'True'}),
            'referred_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_reference'", 'null': 'True', 'to': u"orm['user_app.Professional']"}),
            'shopify_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'youtube': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'user_app.professional': {
            'Meta': {'object_name': 'Professional', '_ormbases': [u'user_app.CustomUser']},
            'certification_name1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'certification_name2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'certification_number1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'certification_number2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'certified_group_fitness': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'certified_nutritionist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['user_app.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fitness_sales_experience': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'group_fitness_experience': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_accepting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nutritionist_experience': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'queue': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['feed']