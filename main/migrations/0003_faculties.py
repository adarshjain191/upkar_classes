# Generated by Django 4.0.2 on 2022-03-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_announcements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('im', models.ImageField(upload_to='')),
                ('faculty_name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=100)),
            ],
        ),
    ]
