# Generated by Django 5.0.2 on 2024-02-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_securekeys_s_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securekeys',
            name='s_key',
            field=models.BinaryField(),
        ),
    ]
