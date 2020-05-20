# Generated by Django 3.0.6 on 2020-05-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('amount', models.BigIntegerField(default=0)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.BigIntegerField(default=0)),
                ('current_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('amount', models.BigIntegerField(default=0)),
                ('payment_ref_id', models.CharField(max_length=255)),
                ('created_at', models.BigIntegerField(default=0)),
            ],
        ),
    ]
