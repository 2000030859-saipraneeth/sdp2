# Generated by Django 4.0.2 on 2022-03-30 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tth', '0002_userreg_trans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usertravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('umode', models.CharField(max_length=100)),
                ('udate', models.DateField(max_length=100)),
                ('utime', models.TimeField(max_length=100)),
                ('ufrom', models.CharField(max_length=100)),
                ('uto', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Travel',
            },
        ),
    ]
