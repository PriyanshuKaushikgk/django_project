# Generated by Django 5.1 on 2024-12-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]