"""Imports"""
from django.db import models


class CustomOrder(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=500, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XLARGE = 'XL'

    SIZES = [
        (SMALL, 'Small: 100cm x 100cm'),
        (MEDIUM, 'Medium: 190cm x 90cm'),
        (LARGE, 'Large: 135cm x 190cm'),
        (XLARGE, 'X Large: 150cm x 200cm'),
    ]
    size = models.CharField(
        max_length=20, blank=False, default=SMALL, choices=SIZES)

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
    MIX = 'Random Mix'

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

    design = models.CharField(
        max_length=100, blank=True, default="", choices=PATTERN_OPTIONS)

    def __str__(self):
        return f'{ self.name }'
