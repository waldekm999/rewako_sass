# Generated by Django 4.2.3 on 2024-02-19 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=24)),
                ("slug", models.SlugField(max_length=24)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, upload_to="categories/%Y/%m/%d"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=125)),
                ("slug", models.SlugField(max_length=125)),
                (
                    "material",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("pcv", "PCV"),
                            ("inox", "INOX"),
                            ("steal", "Stal"),
                            ("plastic", "Tworzywo Sztuczne"),
                            ("inne", ""),
                        ],
                        max_length=24,
                        null=True,
                    ),
                ),
                ("describe", models.TextField()),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("kpl", "kpl"),
                            ("mb", "mb"),
                            ("szt", "szt"),
                            ("kg", "kg"),
                        ],
                        max_length=4,
                    ),
                ),
                ("width", models.IntegerField(blank=True, null=True)),
                ("thickness", models.IntegerField(blank=True, null=True)),
                (
                    "colour",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("black", "Czarny"),
                            ("blue", "Niebieski"),
                            ("green", "Zielony"),
                            ("grey", "Szary"),
                            ("red", "Czerwony"),
                            ("transparent", "Bezbarwny"),
                            ("white", "Biały"),
                            ("yellow", "Żółty"),
                        ],
                        default="transparent",
                        max_length=24,
                        null=True,
                    ),
                ),
                ("isCool", models.BooleanField(blank=True, default=False, null=True)),
                ("ribbed", models.BooleanField(blank=True, default=False, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("available", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "ordering": ("name",),
                "index_together": {("id", "slug")},
            },
        ),
    ]
