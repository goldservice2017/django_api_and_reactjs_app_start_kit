# Generated by Django 2.0.2 on 2018-09-03 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talent', '0009_auto_20180829_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentMedical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_title', models.CharField(blank=True, max_length=300, null=True)),
                ('condition_value', models.BooleanField(default=False)),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent_medicals', to='talent.Talent')),
            ],
            options={
                'db_table': 'talent_medical',
                'ordering': ('talent', 'condition_title', 'condition_value'),
                'managed': True,
            },
        ),
    ]
