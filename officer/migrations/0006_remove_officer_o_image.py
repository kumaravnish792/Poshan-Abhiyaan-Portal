# Generated by Django 3.0.2 on 2020-02-05 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0005_auto_20200202_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='o_image',
        ),
    ]