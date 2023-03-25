# Generated by Django 3.1 on 2023-03-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('w3school_sql', '0002_delete_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=100, verbose_name='Customer name')),
                ('ContactName', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('City', models.CharField(help_text='Please use the following format:    <em>Delhi</em>', max_length=100)),
                ('PostalCode', models.IntegerField(help_text='Please use the following format:    <em>110059</em>')),
                ('Country', models.CharField(help_text='Please use the following format:    <em>India</em>', max_length=100)),
            ],
            options={
                'verbose_name': 'Customer',
            },
        ),
    ]
