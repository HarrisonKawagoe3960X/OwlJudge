# Generated by Django 2.2.6 on 2020-05-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnumber', models.IntegerField()),
                ('answer', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('questionnumber', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('code', models.TextField(null=True)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]