# Generated by Django 5.1.2 on 2024-10-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iana_Spotify', '0006_remove_cancionsimilar_artista_similar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='nombre',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]