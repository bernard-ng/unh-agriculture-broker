# Generated by Django 5.0.1 on 2024-01-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratoire',
            fields=[
                ('id_lab', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('prevision_meteo', models.TextField()),
            ],
            options={
                'db_table': 'laboratoire',
            },
        ),
    ]