# Generated by Django 3.2.5 on 2021-11-17 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_auto_20211117_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('location', models.CharField(max_length=264)),
                ('principle', models.CharField(max_length=264)),
                ('main_branch', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('tenth', models.PositiveIntegerField()),
                ('ninth', models.PositiveIntegerField()),
                ('eighth', models.PositiveIntegerField()),
                ('seventh', models.PositiveIntegerField()),
                ('sixth', models.PositiveIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students', to='school_app.school')),
            ],
        ),
    ]
