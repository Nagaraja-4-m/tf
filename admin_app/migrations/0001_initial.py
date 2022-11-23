# Generated by Django 4.1.3 on 2022-11-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fullname', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=64)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'admins',
            },
        ),
    ]
