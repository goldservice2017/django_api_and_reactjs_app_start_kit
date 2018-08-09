# Generated by Django 2.0.2 on 2018-08-09 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talent', '0005_auto_20180726_1926'),
        ('talent_position_sub_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentAdditionalPositionSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent_additional_position_sub_types', to='talent.Talent')),
                ('talent_position_sub_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent_additional_position_sub_types', to='talent_position_sub_type.TalentPositionSubType')),
            ],
            options={
                'db_table': 'talent_additional_position_sub_type',
                'managed': True,
            },
        ),
    ]
