# Generated by Django 4.1.3 on 2022-11-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PressContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Presscontent',
                'verbose_name_plural': 'PressContents',
                'db_table': 'presscontent',
            },
        ),
    ]
