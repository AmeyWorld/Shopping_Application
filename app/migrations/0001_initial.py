# Generated by Django 3.1.4 on 2021-02-08 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.ImageField(upload_to='')),
                ('state', models.CharField(choices=[('AR|Arunachal Pradesh', 'AR|Arunachal Pradesh'), ('AS|Assam', 'AS|Assam'), ('BR|Bihar', 'BR|Bihar'), ('CT|Chhattisgarh', 'CT|Chhattisgarh'), ('GA|Goa', 'GA|Goa'), ('GJ|Gujarat', 'GJ|Gujarat'), ('HR|Haryana', 'HR|Haryana'), ('HP|Himachal Pradesh', 'HP|Himachal Pradesh'), ('JK|Jammu and Kashmir', 'JK|Jammu and Kashmir'), ('JH|Jharkhand', 'JH|Jharkhand'), ('KA|Karnataka', 'KA|Karnataka'), ('KL|Kerala', 'KL|Kerala'), ('MP|Madhya Pradesh', 'MP|Madhya Pradesh'), ('MH|Maharashtra', 'MH|Maharashtra'), ('MN|Manipur', 'MN|Manipur'), ('ML|Meghalaya', 'ML|Meghalaya'), ('MZ|Mizoram', 'MZ|Mizoram'), ('NL|Nagaland', 'NL|Nagaland'), ('OR|Odisha', 'OR|Odisha'), ('PB|Punjab', 'PB|Punjab'), ('RJ|Rajasthan', 'RJ|Rajasthan'), ('SK|Sikkim', 'SK|Sikkim'), ('TN|Tamil Nadu', 'TN|Tamil Nadu'), ('TG|Telangana', 'TG|Telangana'), ('TR|Tripura', 'TR|Tripura'), ('UT|Uttarakhand', 'UT|Uttarakhand'), ('UP|Uttar Pradesh', 'UP|Uttar Pradesh'), ('WB|West Bengal', 'WB|West Bengal'), ('AN|Andaman and Nicobar Islands', 'AN|Andaman and Nicobar Islands'), ('CH|Chandigarh', 'CH|Chandigarh'), ('DN|Dadra and Nagar Haveli', 'DN|Dadra and Nagar Haveli'), ('DD|Daman and Diu', 'DD|Daman and Diu'), ('DL|Delhi', 'DL|Delhi'), ('LD|Lakshadweep', 'LD|Lakshadweep'), ('PY|Puducherry', 'PY|Puducherry')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Ware'), ('BW', 'Bottom Ware')], max_length=100)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
