# Generated by Django 5.0.3 on 2024-04-01 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
    ]