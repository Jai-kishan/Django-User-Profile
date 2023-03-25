from django.db import models

# Create your models here.


class Customer(models.Model):
    CustomerID = models.AutoField(
        primary_key=True, unique=True, verbose_name="unique id for customer"),
    CustomerName = models.CharField(
        max_length=100, verbose_name="Customer name")
    ContactName = models.CharField(max_length=100)
    Address = models.TextField()
    City = models.CharField(
        max_length=100, help_text="Please use the following format:    <em>Delhi</em>")
    PostalCode = models.CharField(max_length=50)
    Country = models.CharField(
        max_length=100, help_text="Please use the following format:    <em>India</em>")

    # class Meta:
    #     verbose_name = "Customer"
    #     # abstract =True

    def __str__(self):
        return self.CustomerName


class Category(models.Model):
    CategoryID = models.AutoField(unique=True, primary_key=True)
    CategoryName = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.CategoryName


class Employee(models.Model):
    EmployeeID = models.AutoField(unique=True, primary_key=True)
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    BirthDate = models.DateField()
    Photo = models.ImageField(upload_to='emp_img')
    Notes = models.TextField()

    def __str__(self):
        return f"%s %s"%(self.FirstName,self.LastName)


class Shipper(models.Model):
    ShipperID = models.AutoField(unique=True, primary_key=True)
    ShipperName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)

    def __str__(self):
        return self.ShipperName


class Supplier(models.Model):
    SupplierID = models.AutoField(unique=True, primary_key=True)
    SupplierName = models.CharField(max_length=100)
    ContactName = models.CharField(max_length=100)
    Address = models.TextField()
    City = models.CharField(max_length=100)
    PostalCode = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)

    def __str__(self):
        return self.SupplierName


class Order(models.Model):
    OrderID = models.AutoField(unique=True, primary_key=True)
    CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey('Employee', on_delete=models.CASCADE)
    OrderDate = models.DateTimeField(auto_now_add=True)
    ShipperID = models.ForeignKey('Shipper', on_delete=models.CASCADE)

    def __str__(self):
        return self.CustomerID


class Product(models.Model):
    ProductID = models.AutoField(unique=True, primary_key=True)
    ProductName = models.CharField(max_length=100)
    SupplierID = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    CategoryID = models.ForeignKey('Category', on_delete=models.CASCADE)
    Unit = models.IntegerField()
    Price = models.PositiveIntegerField()

    def __str__(self):
        return self.ProductName


class OrderDetail(models.Model):
    OrderDetailID = models.AutoField(unique=True, primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    ProductID = models.ForeignKey('Product', on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.ProductID
