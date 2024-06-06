from django.db import models


# Create your models here.

class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.Zero.value)
    amount = models.IntegerField(default=1)
    discount = models.IntegerField()
    attribute = models.ManyToManyField('Attribute', blank=True, null=True, related_name='attributes')
    # attribute_value = models.ManyToManyField('AttributeValue', blank=True, null=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('blog.Product', on_delete=models.CASCADE, related_name='images')


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name

#
# class AttributeValue(models.Model):
#     attribute_value = models.CharField(max_length=255)

class Customers(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pictures/', blank=True,null=True)
    description = models.TextField()
    vat_number = models.IntegerField(max_length=11)
    invoice_prefix = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Customers"

