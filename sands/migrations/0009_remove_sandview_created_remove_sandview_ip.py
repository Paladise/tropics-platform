# Generated by Django 4.0.6 on 2022-07-30 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sands', '0008_alter_sandview_created_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sandview',
            name='created',
        ),
        migrations.RemoveField(
            model_name='sandview',
            name='ip',
        ),
    ]