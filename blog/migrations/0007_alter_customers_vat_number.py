# Generated by Django 5.0.6 on 2024-06-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_customers_options_alter_customers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='vat_number',
            field=models.IntegerField(max_length=11),
        ),
    ]
