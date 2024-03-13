# Generated by Django 5.0 on 2024-03-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_dicription_instructor_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')], null=True),
        ),
    ]