# Generated by Django 2.0.7 on 2018-07-09 11:13

from django.db import migrations

import safe_relay_service.safe.models


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0006_safemultisigtx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safecreation',
            name='tx_hash',
            field=safe_relay_service.safe.models.HexField(unique=True),
        ),
        migrations.AlterField(
            model_name='safefunding',
            name='deployer_funded_tx_hash',
            field=safe_relay_service.safe.models.HexField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='safefunding',
            name='safe_deployed_tx_hash',
            field=safe_relay_service.safe.models.HexField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='safemultisigtx',
            name='tx_hash',
            field=safe_relay_service.safe.models.HexField(unique=True),
        ),
    ]
