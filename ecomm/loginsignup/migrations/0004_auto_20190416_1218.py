# Generated by Django 2.2 on 2019-04-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsignup', '0003_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
