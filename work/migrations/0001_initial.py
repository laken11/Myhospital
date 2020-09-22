# Generated by Django 3.1 on 2020-09-17 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=50)),
                ('appointment_schedules', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.UUIDField(default=uuid.UUID('3b437aad-acab-47d5-83bb-e526afc5b166'), editable=False)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('role', models.CharField(max_length=50)),
                ('year_of_employment', models.DateField()),
                ('level', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.staff')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=None, max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('occupation', models.CharField(default=None, max_length=50)),
                ('marital_status', models.CharField(default=None, max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('blood_group', models.CharField(default=None, max_length=10)),
                ('genotype', models.CharField(default=None, max_length=5)),
                ('next_of_kin', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=500)),
                ('treatments', models.CharField(max_length=500)),
                ('medications', models.CharField(max_length=500)),
                ('text_result', models.CharField(max_length=500)),
                ('appointment_history', models.DateField()),
                ('updated_date', models.DateField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.patient')),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=150)),
                ('test_id', models.CharField(max_length=10)),
                ('test_result', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.patient')),
                ('Staff', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.DateTimeField()),
                ('appointment_reference', models.UUIDField(default=uuid.UUID('f1773863-6208-4d05-801b-d7edffb5d54e'), editable=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='work.patient')),
            ],
        ),
    ]
