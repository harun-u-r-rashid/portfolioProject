# Generated by Django 5.0.3 on 2024-06-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProject', '0002_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreview',
            name='review',
            field=models.TextField(max_length=200),
        ),
    ]
