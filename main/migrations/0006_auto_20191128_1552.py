# Generated by Django 2.2.6 on 2019-11-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_customer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitelogs',
            name='user_log_date',
        ),
        migrations.AddField(
            model_name='websitelogs',
            name='log',
            field=models.CharField(default='log', max_length=30),
        ),
        migrations.AddField(
            model_name='websitelogs',
            name='user_log',
            field=models.CharField(default='log', max_length=30),
        ),
        migrations.AlterField(
            model_name='websitelogs',
            name='user_id',
            field=models.SmallIntegerField(default=1),
        ),
    ]
