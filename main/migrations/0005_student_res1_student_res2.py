# Generated by Django 4.1.1 on 2022-12-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_image_student_limage_student_rimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='res1',
            field=models.CharField(default='', max_length=22),
        ),
        migrations.AddField(
            model_name='student',
            name='res2',
            field=models.CharField(default='', max_length=22),
        ),
    ]
