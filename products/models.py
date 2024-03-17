from decimal import Decimal, ROUND_HALF_UP

from django.db import models
from django.urls import reverse

"""
def category_image_upload_path(instance, filename):
    # Generate file path for category images
    return os.path.join('images/category_images', filename)


class AllProductsManager(models.Manager):
    def get_queryset(self):
        return super(AllProductsManager, self).get_queryset().all()
        
        """


class Category(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    UNIT_CHOICES = (
        ('kpl', 'kpl'),
        ('mb', 'mb'),
        ('szt', 'szt'),
        ('kg', 'kg'),
    )
    MATERIAL_CHOICES = (
        ('pcv', 'PCV'),
        ('inox', 'INOX'),
        ('steal', 'Stal'),
        ('plastic', 'Tworzywo Sztuczne'),
        ('inne', '')
    )
    COLOR_CHOOSES = (
        ('black', 'Czarny'),
        ('blue', 'Niebieski'),
        ('green', 'Zielony'),
        ('grey', 'Szary'),
        ('red', 'Czerwony'),
        ('transparent', 'Bezbarwny'),
        ('white', 'Biały'),
        ('yellow', 'Żółty'),
    )
    TAX_CHOICES = (
        (0, '0%'),
        (5, '5%'),
        (8, '8%'),
        (23, '23%')
    )
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125)
    material = models.CharField(max_length=24, choices=MATERIAL_CHOICES, blank=True, null=True)
    describe = models.TextField()
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    width = models.IntegerField(blank=True, null=True)
    thickness = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=24, choices=COLOR_CHOOSES, blank=True, null=True)
    isCool = models.BooleanField(default=False, blank=True, null=True)
    ribbed = models.BooleanField(default=False, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.IntegerField(choices=TAX_CHOICES, default=23)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    @property
    def gross_price(self):
        # Calculate the gross price using the price and tax fields
        if self.tax == 0:
            return self.price
        else:
            tax_multiplier = Decimal(1 + (self.tax / 100))
            gross_price = self.price * tax_multiplier
            gross_price = gross_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
            return gross_price

    class Meta:
        ordering = ('name',)
        index_together = [('id', 'slug'), ]
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
