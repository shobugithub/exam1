# Generated by Django 5.0.6 on 2024-06-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_product_attribute_delete_productattribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('billing_address', models.CharField(max_length=255)),
                ('iamge', models.ImageField(upload_to='profile_pictures/')),
                ('description', models.TextField()),
                ('vat_number', models.CharField(max_length=255)),
                ('invoice_prefix', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='attribute',
            field=models.ManyToManyField(blank=True, null=True, related_name='attributes', to='blog.attribute'),
        ),
    ]
