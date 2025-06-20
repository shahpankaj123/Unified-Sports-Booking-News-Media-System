# Generated by Django 5.2 on 2025-05-11 10:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='GenderID',
            field=models.UUIDField(default=uuid.UUID('6f785490-0547-44ba-ab73-3e635058644e'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='otpdata',
            name='OTPDataID',
            field=models.UUIDField(default=uuid.UUID('f54c8071-ee9f-4c89-b932-b1eac6cbcd24'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='PaymentTypeID',
            field=models.UUIDField(default=uuid.UUID('b63e49cb-f2ee-416f-85cd-177394c3903a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
