# Generated by Django 4.2.13 on 2024-08-11 07:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_accordionitem_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accordionitem',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
