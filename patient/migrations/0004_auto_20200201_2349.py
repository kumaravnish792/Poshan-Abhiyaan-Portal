# Generated by Django 3.0.2 on 2020-02-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_aadhaar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
