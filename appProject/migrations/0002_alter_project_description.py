# Generated by Django 5.0.3 on 2024-06-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
