# Generated by Django 3.1.5 on 2021-05-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme_curriculum', '0003_auto_20210506_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='percent_lab_evaluation',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='percent_endsem',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='percent_quiz_2',
            field=models.PositiveIntegerField(default=10),
        ),
    ]