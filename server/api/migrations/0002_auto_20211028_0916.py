# Generated by Django 3.1.7 on 2021-10-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='log',
            name='title',
        ),
        migrations.AddField(
            model_name='log',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='direction',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='group',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='photo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='plate_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='status',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='sync',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='type_passage',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='uuid',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
