# Generated by Django 2.0.2 on 2018-07-26 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0004_talent_talent_position_sub_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='talent_position_sub_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='talents', to='talent_position_sub_type.TalentPositionSubType'),
        ),
    ]
