# Generated by Django 3.1 on 2020-11-23 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='start_time',
        ),
        migrations.AddField(
            model_name='appointments',
            name='slot',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(default='General', max_length=40),
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkups', to='users.doctor'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='TempAppointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField()),
                ('slot', models.TimeField()),
                ('disease', models.ManyToManyField(to='users.Disease')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.TimeField(auto_now=True)),
                ('slot2', models.TimeField(auto_now=True)),
                ('slot3', models.TimeField(auto_now=True)),
                ('slot4', models.TimeField(auto_now=True)),
                ('slot5', models.TimeField(auto_now=True)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='users.doctor')),
            ],
        ),
    ]