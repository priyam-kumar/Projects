# Generated by Django 2.2.5 on 2019-09-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentsrecord',
            fields=[
                ('registration_no', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('father_email', models.CharField(max_length=30)),
            ],
        ),
    ]
