# Generated by Django 4.1.4 on 2022-12-09 08:34

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[(api.models.RoleChoice['ow'], 'Owner'), (api.models.RoleChoice['Hi'], 'Hirer'), (api.models.RoleChoice['Ad'], 'Admin')], max_length=2)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
