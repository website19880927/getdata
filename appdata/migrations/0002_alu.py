# Generated by Django 2.0.6 on 2018-12-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 't_num',
            },
        ),
    ]
