# Generated by Django 4.0.4 on 2022-06-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0003_delete_hotelrecord_delete_personalinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=1000)),
                ('Email', models.EmailField(max_length=254)),
                ('Occupation', models.CharField(max_length=1000)),
                ('Room_Number', models.IntegerField()),
                ('Amount_Paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Number_Of_Nights', models.IntegerField()),
                ('Day_Of_Arrival', models.DateField()),
                ('Day_Of_Departure', models.DateField()),
            ],
        ),
    ]
