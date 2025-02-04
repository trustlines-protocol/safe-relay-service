# Generated by Django 2.2 on 2019-04-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relay", "0016_internaltx_error"),
    ]

    operations = [
        migrations.AddField(
            model_name="internaltx",
            name="trace_address",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="internaltx",
            unique_together={("ethereum_tx", "trace_address")},
        ),
        migrations.RemoveField(
            model_name="internaltx",
            name="transaction_index",
        ),
    ]
