# Generated by Django 5.0.2 on 2024-04-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0003_alter_teammembers_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='position',
            field=models.CharField(choices=[('Volunteer', 'Volunteer'), ('Member', 'Member'), ('Admin', 'Admin')], max_length=100),
        ),
    ]
