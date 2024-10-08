# Generated by Django 5.0.2 on 2024-02-27 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='до 100 символов', max_length=100, null=True, verbose_name='Meta Title')),
                ('description', models.TextField(blank=True, help_text='до 150 символов', null=True, validators=[django.core.validators.MaxLengthValidator(150)], verbose_name='Meta Description')),
                ('telegram', models.CharField(blank=True, help_text='до 100 символов', max_length=100, null=True, verbose_name='Telegram')),
                ('email', models.EmailField(blank=True, help_text='до 100 символов', max_length=100, null=True, verbose_name='Email')),
                ('favicon_ico', models.FileField(blank=True, null=True, upload_to='media', verbose_name='favicon (.ico)')),
                ('favicon_png', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='favicon (.png)')),
            ],
        ),
    ]
