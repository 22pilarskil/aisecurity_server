# Generated by Django 2.2.5 on 2019-09-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190920_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdateinoutstatus',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
