# Generated by Django 2.1.7 on 2019-03-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelChain',
            fields=[
                ('hotel_chain_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_chain_code', models.CharField(max_length=10)),
                ('hotel_chain', models.CharField(max_length=50)),
            ],
        ),
    ]
