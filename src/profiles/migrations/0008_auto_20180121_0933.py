# Generated by Django 2.0.1 on 2018-01-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20180121_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
