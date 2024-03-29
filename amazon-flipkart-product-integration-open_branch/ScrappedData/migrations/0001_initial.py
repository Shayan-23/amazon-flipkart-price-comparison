# Generated by Django 4.0 on 2021-12-24 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmezonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.SlugField(blank=True, max_length=500, null=True)),
                ('review_num', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('product_description', models.CharField(blank=True, max_length=600, null=True)),
                ('product_link', models.SlugField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='FlipkartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.SlugField(blank=True, max_length=500, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('ratting', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('review_data', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('discount', models.CharField(blank=True, max_length=100, null=True)),
                ('original_price', models.IntegerField(blank=True, null=True)),
                ('product_description', models.CharField(blank=True, max_length=600, null=True)),
                ('product_link', models.SlugField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amazon_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ScrappedData.amezondata')),
                ('flipkart_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ScrappedData.flipkartdata')),
            ],
        ),
    ]
