# Generated by Django 3.1.2 on 2020-10-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201017_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]
