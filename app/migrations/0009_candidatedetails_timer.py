# Generated by Django 4.1.4 on 2023-03-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_candidatedetails_sheet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatedetails',
            name='timer',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
