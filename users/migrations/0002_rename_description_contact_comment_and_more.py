# Generated by Django 4.1.4 on 2022-12-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phoneNumber',
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=158),
        ),
    ]
