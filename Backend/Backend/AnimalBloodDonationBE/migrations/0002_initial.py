# Generated by Django 4.0.5 on 2022-08-14 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AnimalBloodDonationBE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalBloodDonationBE.case'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalBloodDonationBE.owner'),
        ),
        migrations.AddField(
            model_name='caseimage',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalBloodDonationBE.case'),
        ),
        migrations.AddField(
            model_name='case',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalBloodDonationBE.pet'),
        ),
    ]
