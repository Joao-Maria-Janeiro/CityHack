# Generated by Django 2.1.2 on 2019-05-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeMCU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=100)),
                ('monthly_budget', models.IntegerField(default=-1)),
            ],
        ),
    ]