# Generated by Django 2.2.2 on 2019-07-01 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20190701_1632'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSignUpForm',
            new_name='Newsletter',
        ),
    ]
