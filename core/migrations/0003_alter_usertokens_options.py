# Generated by Django 4.0.4 on 2022-05-08 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usertokens_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertokens',
            options={'verbose_name': 'User Token', 'verbose_name_plural': 'User Tokens'},
        ),
    ]
