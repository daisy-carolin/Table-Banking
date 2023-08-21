# Generated by Django 4.2.4 on 2023-08-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_userregistation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('number_of_members', models.PositiveIntegerField()),
                ('group_type', models.CharField(choices=[('savings', 'Savings Group'), ('loan', 'Loan Group')], max_length=20)),
                ('group_role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member')], max_length=20)),
                ('country_of_operation', models.CharField(max_length=50)),
                ('group_currency', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('KES', 'Kenyan Shilling')], max_length=3)),
            ],
        ),
    ]