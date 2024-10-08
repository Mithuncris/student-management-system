# Generated by Django 5.1.1 on 2024-10-03 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('class_enrolled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
            ],
        ),
    ]
