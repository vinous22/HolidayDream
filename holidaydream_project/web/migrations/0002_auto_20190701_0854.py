# Generated by Django 2.2.2 on 2019-07-01 06:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogIndexPage',
            new_name='FeaturedIndexPage',
        ),
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='FeaturedPage',
        ),
    ]
