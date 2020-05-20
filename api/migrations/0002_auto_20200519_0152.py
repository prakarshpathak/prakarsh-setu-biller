# Generated by Django 3.0.6 on 2020-05-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='remaining_amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='receipt',
            name='platform_txn_ref_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bill',
            name='created_at',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='created_at',
            field=models.DateTimeField(default=0),
        ),
    ]