# Generated by Django 2.1.7 on 2019-05-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_house', '0004_auto_20190424_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('contact_number', models.IntegerField(max_length=15)),
                ('idproof', models.FileField(upload_to='uploads/')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
    ]
