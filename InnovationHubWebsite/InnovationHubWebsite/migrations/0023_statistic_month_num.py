# Generated by Django 2.0.4 on 2018-12-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0022_auto_20181219_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='month_num',
            field=models.IntegerField(null=True),
        ),
    ]
