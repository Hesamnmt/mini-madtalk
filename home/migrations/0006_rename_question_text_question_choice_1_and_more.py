# Generated by Django 4.2 on 2023-05-31 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_choice_choice_1_alter_choice_choice_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='choice_1',
        ),
        migrations.AddField(
            model_name='question',
            name='choice_2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='choice_3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='choice_4',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='correct_choice',
            field=models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
