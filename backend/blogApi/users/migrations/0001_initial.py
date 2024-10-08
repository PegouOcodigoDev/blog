# Generated by Django 5.1 on 2024-08-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=150)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['name'],
            },
        ),
    ]
