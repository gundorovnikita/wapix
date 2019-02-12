from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug' : self.slug})

    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('mark_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

class Product(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField()
    image = models.ImageField()
    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug' : self.slug})

    def __str__(self):
        return self.slug

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)
