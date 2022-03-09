# Generated by Django 4.0.1 on 2022-03-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('head1', models.CharField(max_length=100)),
                ('chead1', models.CharField(max_length=3000)),
                ('head2', models.CharField(max_length=100)),
                ('chead2', models.CharField(max_length=3000)),
                ('head3', models.CharField(max_length=100)),
                ('chead3', models.CharField(max_length=3000)),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]