# Generated by Django 4.0.5 on 2022-07-01 16:33

import django.core.validators
from django.db import migrations, models
import users.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=150)),
                ('id_num', models.CharField(error_messages={'wrong': 'sorry you may not a student or teacher of the department.'}, max_length=8, validators=[django.core.validators.RegexValidator('^[0-9]{2}[1-9]0[0-9][0-9]{3}$', code='wrong')])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
