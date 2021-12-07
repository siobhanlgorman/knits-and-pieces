from django.db import models


class Category(models.Model):
    """A model for the product category"""
    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80, blank=True, default="")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tag(models.Model):
    """A model for a tag for a special addition to a product"""


class Product(models.Model):
    """A model for the product"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    ITEM_SIZES = (
        ('os', 'One Size'),
        ('xs', 'Extra-Small'),
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('xl', 'Extra-Large'),
    )
    size = models.CharField(max_length=100, choices=ITEM_SIZES)
    description = models.TextField()
    tag = models.ForeignKey(
        'Tag', null=True, blank=True, on_delete=models.SET_NULL, max_length=99)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    material = models.CharField(max_length=100)
    machine_wash = models.BooleanField(default=True)
    product_image1 = models.ImageField()
    product_image1 = models.ImageField(null=True, blank=True)
    product_image1 = models.ImageField(null=True, blank=True)
    shade_type = models.CharField(max_length=50, blank=True, default="")
    colour1 = models.CharField(max_length=50, blank=True, default="")
    colour1 = models.CharField(max_length=50, blank=True, default="")
    colour1 = models.CharField(max_length=50, blank=True, default="")
    colour1 = models.CharField(max_length=50, blank=True, default="")
    pattern_name = models.CharField(max_length=100, blank=True, default="")
    designer = models.CharField(max_length=50, blank=True, default="")
    can_custom_design = models.BooleanField(default=False)
    likes = models.ManyToManyField('User')
