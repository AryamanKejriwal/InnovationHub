# Generated by Django 2.0.4 on 2018-06-26 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0003_featuredprints_recentprints'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeaturedPrints',
            new_name='FeaturedPrint',
        ),
        migrations.RenameModel(
            old_name='RecentPrints',
            new_name='RecentPrint',
        ),
    ]
