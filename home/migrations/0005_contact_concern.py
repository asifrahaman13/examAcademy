# Generated by Django 4.0.1 on 2022-03-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_contact_concern'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='concern',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
