# Generated by Django 4.0.4 on 2022-04-27 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0005_fooditem_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='child',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.booking')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.fooditem')),
            ],
            options={
                'db_table': 'bookingitems',
            },
        ),
    ]