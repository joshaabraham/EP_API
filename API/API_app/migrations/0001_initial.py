# Generated by Django 3.2.7 on 2021-09-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('PhraseID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('UtilisateurID', models.AutoField(primary_key=True, serialize=False)),
                ('UtilisateurNom', models.CharField(max_length=100)),
                ('UtilisateurEmail', models.EmailField(max_length=200)),
            ],
        ),
    ]
