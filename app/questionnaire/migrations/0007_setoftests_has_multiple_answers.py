# Generated by Django 4.1.7 on 2023-04-25 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_alter_test_set_of_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='setoftests',
            name='has_multiple_answers',
            field=models.BooleanField(default=False),
        ),
    ]
