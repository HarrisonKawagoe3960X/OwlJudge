# Generated by Django 2.2.6 on 2020-05-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='sinput',
            field=models.TextField(null=True),
        ),
    ]
