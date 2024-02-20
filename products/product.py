from django.db import models

"""
def product_image_upload_path(instance, filename):
    # Generate file path for category images
    return os.path.join('images/product_images', filename)
    """


class Product(models.Model):
    UNIT_CHOICES = (
        ('kpl', 'kpl'),
        ('mb', 'mb'),
        ('szt', 'szt'),
    )
    MATERIAL_CHOICES = (
        ('pcv', 'PCV'),
        ('nox', 'NOX'),
        ('stal', 'Stal'),
        ('plastic', 'Tworzywo Sztuczne'),
        ('inne', '')
    )
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125)
    material = models.CharField(max_length=24, choices=MATERIAL_CHOICES, null=True)
    describe = models.TextField(null=True)
    special_description = models.CharField(max_length=64, default='brak', blank=True)
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    is_active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = [('id', 'slug'), ]

    def __str__(self):
        return self.name
