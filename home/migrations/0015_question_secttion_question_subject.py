# Generated by Django 4.2 on 2023-06-07 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_examstudent_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='secttion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.subject'),
            preserve_default=False,
        ),
    ]
