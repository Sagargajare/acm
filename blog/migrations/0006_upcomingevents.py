# Generated by Django 3.1.1 on 2021-01-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_updates_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=300, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('coOrdinatorSpeaker', models.CharField(max_length=100)),
            ],
        ),
    ]
