from django.db import models
from rest_framework import serializers


class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=150)
    Description = models.CharField(max_length=250, null=True)
    Price = models.FloatField()
    StockQuantity = models.IntegerField()
    Category = models.CharField(max_length=150)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.Name


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
