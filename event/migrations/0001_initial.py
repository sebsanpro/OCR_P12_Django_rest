# Generated by Django 3.2.9 on 2021-12-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('status', models.CharField(choices=[('CRE', 'Created'), ('AFF', 'Affected'), ('END', 'Ended')], default='CRE', max_length=3, verbose_name='Event Status')),
                ('attendees', models.PositiveIntegerField(default=1, verbose_name='Attendees person')),
                ('event_date', models.DateTimeField(verbose_name='Event date')),
                ('note', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['client'],
            },
        ),
    ]
