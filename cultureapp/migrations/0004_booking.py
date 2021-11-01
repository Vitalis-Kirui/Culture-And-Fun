# Generated by Django 3.2.8 on 2021-11-01 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cultureapp', '0003_visitplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=30)),
                ('mobile', models.IntegerField()),
                ('vehicle_type', models.CharField(choices=[('', 'Choose Vehicle Type'), ('One Person', 'One Person'), ('Two-Three People', 'Two-Three People'), ('Family Vacation', 'Family Vacation'), ('Educational ', 'Educational '), ('Staff Get Together', 'Staff Get Together'), ('Filming', 'Filming')], default=0, max_length=50)),
                ('appointment_date', models.CharField(blank=True, max_length=30)),
                ('timeframe', models.CharField(choices=[('', 'Choose Time Frame'), ('Single Day', 'Single Day'), ('Weekend(2-3 days)', 'Weekend(2-3 days)'), ('One week(1+ week)', 'One week(1+ week)')], default=0, max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('plan', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cultureapp.visitplan')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
