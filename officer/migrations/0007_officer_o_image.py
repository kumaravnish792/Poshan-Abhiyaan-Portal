# Generated by Django 3.0.2 on 2020-02-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0006_remove_officer_o_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='o_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
