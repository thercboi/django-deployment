# Generated by Django 3.2.5 on 2021-11-16 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_school_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
