# Generated by Django 3.2.5 on 2021-07-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=20)),
                ('Contact_person', models.CharField(max_length=20)),
                ('Mobile_number', models.CharField(max_length=10)),
            ],
        ),
    ]
