# Generated by Django 3.0.2 on 2020-02-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0007_officer_o_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='login_number',
            field=models.CharField(default='NILL', max_length=30),
        ),
    ]
