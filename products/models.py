"""Imports"""
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """A model for the product category"""
    class Meta:
        """Set spelling of category plural in admin panel"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80, blank=True, default="")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tag(models.Model):
    """A model for a tag for a special addition to a product"""
    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80, blank=True, default="")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """A model for the product"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)

    ONE_SIZE = 'OS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    ITEM_SIZES = [
        (ONE_SIZE, 'One Size'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    item_sizes = models.CharField(
        max_length=20, blank=False, default=ONE_SIZE, choices=ITEM_SIZES)
    description = models.TextField()
    tag = models.ForeignKey(
        'Tag', null=True, blank=True, on_delete=models.SET_NULL, max_length=99)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    ACRYLIC = 'AC'
    COTTON = 'CN'
    ACRYLIC_WOOL_MIX = 'AW'

    MATERIAL_TYPE = [
        (ACRYLIC, '100% Acrylic'),
        (COTTON, '100% Cotton'),
        (ACRYLIC_WOOL_MIX, '70% Acrylic, 30% Wool')
    ]

    material = models.CharField(
        max_length=2, blank=False, default=ACRYLIC, choices=MATERIAL_TYPE)
    machine_wash = models.BooleanField(default=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    RED = 'RED'
    ORANGE = 'OR'
    GREEN = 'GRN'
    BLUE = 'BLU'
    PINK = 'PI'
    YELLOW = 'YE'
    TEAL = 'TEA'
    GREY = 'GRY'
    PURPLE = 'PU'
    TURQUOISE = 'TU'
    BLACK = 'BLA'
    WHITE = 'WH'
    CREAM = 'CR'
    BEIGE = 'BEI'
    BROWN = 'BR'
    MAROON = 'MR'

    COLOUR_OPTIONS = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (PINK, 'Pink'),
        (YELLOW, 'Yellow'),
        (TEAL, 'Teal'),
        (GREY, 'Grey'),
        (PURPLE, 'Purple'),
        (TURQUOISE, 'Turquoise'),
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (CREAM, 'Cream'),
        (BEIGE, 'Beige'),
        (BROWN, 'Brown'),
        (MAROON, 'Maroon')
        ]

    colour1 = models.CharField(
        max_length=50, blank=False, choices=COLOUR_OPTIONS)
    colour2 = models.CharField(
        max_length=50, blank=True, default="", choices=COLOUR_OPTIONS)
    colour3 = models.CharField(
        max_length=50, blank=True, default="", choices=COLOUR_OPTIONS)
    colour4 = models.CharField(
        max_length=50, blank=True, default="", choices=COLOUR_OPTIONS)

    DREAMS = 'Dreams'
    SUN = 'Sun'
    FLOWER = 'Flower'
    ICE = 'Ice'
    STRIPE = 'Stripe'
    GRANNY = 'Granny'
    STRIPE_SPIKE = 'Spiked Stripe'
    LACY_SUN = 'Lacy Sun'
    MIX = 'Mix'

    PATTERN_OPTIONS = [
        (DREAMS, 'Dreams'),
        (SUN, 'Sun'),
        (FLOWER, 'Flower'),
        (ICE, 'Ice'),
        (STRIPE, 'Stripe'),
        (GRANNY, 'Granny'),
        (STRIPE_SPIKE, 'Spiked Stripe'),
        (LACY_SUN, 'Lacy Sun'),
        (MIX, 'Mix'),
    ]

    pattern_name = models.CharField(
        max_length=100, blank=True, default="", choices=PATTERN_OPTIONS)
    designer = models.CharField(max_length=50, blank=True, default="")
    can_custom_design = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='product_likes', blank=True)

    def __str__(self):
        return self.name
