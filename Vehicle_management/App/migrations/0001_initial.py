# Generated by Django 4.2.4 on 2023-08-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=150)),
                ('Type', models.CharField(choices=[('two', 'Two'), ('three', 'Three'), ('four', 'Four')], max_length=10)),
                ('model', models.TextField(default=' ', max_length=300)),
                ('description', models.TextField(default=' ', max_length=300)),
            ],
        ),
    ]