# Generated by Django 5.0 on 2024-03-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='dicription',
            new_name='description',
        ),
        migrations.AddField(
            model_name='instructor',
            name='courses_teched_before',
            field=models.IntegerField(choices=[(0, '0 courses'), (1, '1 course'), (2, '2 courses'), (3, '3 courses'), (4, '4 courses'), (5, '5 or more than 5 courses')], default=0),
        ),
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.CharField(default='o', max_length=150),
        ),
        migrations.AddField(
            model_name='instructor',
            name='phone_num',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]
