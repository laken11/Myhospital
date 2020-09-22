# Generated by Django 3.1 on 2020-09-18 21:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20200918_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointments',
            name='appointment_reference',
            field=models.UUIDField(default=uuid.UUID('6a6c74e2-e2ee-4801-ae08-07f4dbdb6b8a'), editable=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.UUIDField(default=uuid.UUID('627f6989-e068-4738-992e-c761ab2d1dfa'), editable=False),
        ),
    ]
