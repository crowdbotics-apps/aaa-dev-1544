# Generated by Django 2.2.9 on 2020-02-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='aaa',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
