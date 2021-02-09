from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
STATE_CHOICES = (
('AR|Arunachal Pradesh','AR|Arunachal Pradesh'),('AS|Assam','AS|Assam'),
('BR|Bihar','BR|Bihar'),('CT|Chhattisgarh','CT|Chhattisgarh'),
('GA|Goa','GA|Goa'),('GJ|Gujarat','GJ|Gujarat'),
('HR|Haryana','HR|Haryana'),('HP|Himachal Pradesh','HP|Himachal Pradesh'),
('JK|Jammu and Kashmir','JK|Jammu and Kashmir'),('JH|Jharkhand','JH|Jharkhand'),
('KA|Karnataka','KA|Karnataka'),('KL|Kerala','KL|Kerala'),('MP|Madhya Pradesh','MP|Madhya Pradesh'),
('MH|Maharashtra','MH|Maharashtra'),('MN|Manipur','MN|Manipur'),('ML|Meghalaya','ML|Meghalaya'),
('MZ|Mizoram','MZ|Mizoram'),('NL|Nagaland','NL|Nagaland'),('OR|Odisha','OR|Odisha'),
('PB|Punjab','PB|Punjab'),('RJ|Rajasthan','RJ|Rajasthan'),('SK|Sikkim','SK|Sikkim'),
('TN|Tamil Nadu','TN|Tamil Nadu'),('TG|Telangana','TG|Telangana'),('TR|Tripura','TR|Tripura'),
('UT|Uttarakhand','UT|Uttarakhand'),('UP|Uttar Pradesh','UP|Uttar Pradesh'),
('WB|West Bengal','WB|West Bengal'),('AN|Andaman and Nicobar Islands','AN|Andaman and Nicobar Islands'),
('CH|Chandigarh','CH|Chandigarh'),('DN|Dadra and Nagar Haveli','DN|Dadra and Nagar Haveli'),
('DD|Daman and Diu','DD|Daman and Diu'),('DL|Delhi','DL|Delhi'),
('LD|Lakshadweep','LD|Lakshadweep'),('PY|Puducherry','PY|Puducherry')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'customer'

CATEGORY_CHOICE = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Ware'),
    ('BW','Bottom Ware'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=100)
    product_image = models.ImageField(upload_to = 'productimg') 

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return  self.quantity * self.product.discounted_price

STATUS_CHOICES =(
('Accepted','Accepted'),
('Packed','Packed'),
('On The Way','On The Way'),
('Delivered','Delivered'),
('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)
    order_date = models.DateTimeField(auto_now_add= True)
    status =  models.CharField(choices=STATUS_CHOICES, max_length=100, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price