from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female')
)

PRESENT_TYPE = (
    ('full-day', 'Full Day'),
    ('half-day','Half Day'),
    ('absent', 'Absent')
)

class Owner(models.Model): #Done
    first_name = models.CharField(max_length=100)
    last_name = CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.first_name

class Estate(models.Model): #Done
    estate_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.estate_name

class Worker(models.Model): #Done
    epf_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField (max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(max_length=20)
    join_date = models.DateField(max_length=20)
    hourly_rate = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    estate = models.ForeignKey(Estate, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
        return self.first_name

class OwnerEstate(models.Model): #Done
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, null=True)
    estate = models.ForeignKey(Estate, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __int__(self):
        return self.owner

class Attendance(models.Model): #Done
    id = models.AutoField(primary_key=True)
    epf_number = models.ForeignKey(Worker, on_delete=DO_NOTHING, null=True)
    present_date = models.DateField(null=False)
    present_type = models.CharField(max_length=10, choices=PRESENT_TYPE, default='absent')
    recorded_by = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    @property
    def name(self):
        return self.epf_number.first_name

class DailyTeaPlucked(models.Model): #Done
    epf_number = models.ForeignKey(Worker, on_delete=DO_NOTHING, null=True)
    working_date = models.DateField(null=False)
    green_leaf_quantity = models.IntegerField()
    recorded_by = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __int__(self):
        return self.epf_number

class Officer(models.Model): #Done
    epf_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField (max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField(max_length=20)
    #Designation = models.CharField(max_length=100)
    estate = models.ForeignKey(Estate, on_delete=DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.first_name

class Supplier(models.Model):
    company_name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.company_name

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    estate_id = models.ForeignKey(Estate, on_delete=DO_NOTHING, null=True)
    unit = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    item_category = models.CharField(max_length=100)
    quantity_in_hand = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.item_name


class ItemSupplier(models.Model):
    item = models.ForeignKey(Item, on_delete=DO_NOTHING, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.item

class Allowances(models.Model):
    epf_number = models.ForeignKey(Worker, Officer, null=True)
    allowance_amount = models.DecimalField(max_digits=7, decimal_places=2)
    allowance_description = models.CharField(max_length=400)
    active = models.BooleanField()
    start_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.epf_number

class Deductions(models.Model):
    epf_number = models.ForeignKey(Worker, Officer, null=True)
    deduction_amount = models.DecimalField(max_digits=7, decimal_places=2)
    deduction_description = models.CharField(max_length=400)
    start_date = models.DateField(null=True)
    active = models.BooleanField()
    user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.epf_number
