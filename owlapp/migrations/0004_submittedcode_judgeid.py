# Generated by Django 3.0.7 on 2020-06-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owlapp', '0003_auto_20200626_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedcode',
            name='judgeid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]