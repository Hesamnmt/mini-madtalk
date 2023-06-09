# Generated by Django 4.2 on 2023-05-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_exam_subject_exam_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='article_files/'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='homework_files/'),
        ),
    ]
