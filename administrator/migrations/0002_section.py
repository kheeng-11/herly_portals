# Generated by Django 5.1.7 on 2025-03-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=255)),
                ('section_added_on', models.CharField(max_length=255)),
            ],
        ),
    ]
