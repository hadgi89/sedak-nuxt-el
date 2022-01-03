# Generated by Django 3.2.9 on 2021-11-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Адрес e-mail')),
                ('surname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('fathername', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
