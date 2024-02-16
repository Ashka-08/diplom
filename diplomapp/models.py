from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()

    @property
    def photo_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url

    def __str__(self):
        return f'Category_ID:{self.pk} {self.name}'


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def photo_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url

    def __str__(self):
        return f'Category_ID:{self.pk} {self.name}'


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'User_ID:{self.pk} {self.name}, email: {self.email}, \
            phone: {self.phone_number}'


class Unit(models.Model):
    unit_of_measurement = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Unit_ID: {self.pk} {self.unit_of_measurement}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    foto = models.ImageField()
    
    @property
    def photo_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url

    def __str__(self):
        return f'ProductID: {self.pk} {self.name}, price: {self.price}'


class Status(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f'Status_ID {self.pk} {self.status}'


class Order(models.Model):
    order_number = models.CharField(max_length=6)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order №{self.pk}, total price: {self.total_price}'
