# Generated by Django 2.0.4 on 2018-06-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnovationHubWebsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user_id',
            new_name='fk_user',
        ),
        migrations.AddField(
            model_name='job',
            name='file_path',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
