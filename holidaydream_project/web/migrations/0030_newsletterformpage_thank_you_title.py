# Generated by Django 2.2.2 on 2019-07-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_auto_20190711_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterformpage',
            name='thank_you_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
