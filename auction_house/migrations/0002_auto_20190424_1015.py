# Generated by Django 2.1.7 on 2019-04-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='carving_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('pub_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('discription', models.TextField()),
                ('artist_name', models.CharField(max_length=100)),
                ('produced_date', models.DateField()),
                ('auction_date', models.DateField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='drawing_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('pub_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('discription', models.TextField()),
                ('artist_name', models.CharField(max_length=100)),
                ('produced_date', models.DateField()),
                ('auction_date', models.DateField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='painting_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('pub_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('discription', models.TextField()),
                ('artist_name', models.CharField(max_length=100)),
                ('produced_date', models.DateField()),
                ('auction_date', models.DateField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='photographic_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('pub_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('discription', models.TextField()),
                ('artist_name', models.CharField(max_length=100)),
                ('produced_date', models.DateField()),
                ('auction_date', models.DateField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='sculpture_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('pub_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('discription', models.TextField()),
                ('artist_name', models.CharField(max_length=100)),
                ('produced_date', models.DateField()),
                ('auction_date', models.DateField()),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
