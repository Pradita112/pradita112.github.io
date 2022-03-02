# Generated by Django 3.2 on 2022-03-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=45)),
                ('artist', models.CharField(max_length=45)),
                ('tanggal_rilis', models.DateField()),
                ('gambar', models.ImageField(upload_to='album')),
            ],
            options={
                'db_table': 'album',
            },
        ),
    ]
