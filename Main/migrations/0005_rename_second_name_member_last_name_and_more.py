# Generated by Django 4.2.3 on 2023-08-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_member_remove_contribution_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='second_name',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
