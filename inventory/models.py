from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    note = models.TextField()
    stock = models.IntegerField()
    availiability = models.BooleanField(default=False)
    supplier = models.ForeignKey(
        Supplier, default=1, verbose_name='Suppliers', on_delete=models.CASCADE)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Inventory"

        def __str__(self):
            return self.name
