# Generated by Django 2.1.7 on 2019-03-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0007_auto_20190316_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='giata_code',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='gwg_code',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='i5_code',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='emails',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
    ]