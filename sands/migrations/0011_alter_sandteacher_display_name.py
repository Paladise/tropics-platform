# Generated by Django 4.0.6 on 2022-07-30 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sands', '0010_sandteacher_delete_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandteacher',
            name='display_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'The field must contain at least 5 characters.')]),
        ),
    ]
