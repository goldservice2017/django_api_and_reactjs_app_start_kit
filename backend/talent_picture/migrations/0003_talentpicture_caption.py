# Generated by Django 2.0.2 on 2018-08-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_picture', '0002_talentpicture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentpicture',
            name='caption',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
