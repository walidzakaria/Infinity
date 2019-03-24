# Generated by Django 2.1.7 on 2019-03-24 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0014_auto_20190324_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarRating',
            fields=[
                ('star_rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('star_rating_code', models.CharField(max_length=10)),
                ('star_rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.StarRating'),
        ),
    ]
