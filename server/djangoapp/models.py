from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
# User model
class CarMake(models.Model):
    car_make = models.CharField(null=False, max_length=30, default='CarMake')
    description = models.CharField(max_length=500)
    # Create a toString method for object string representation
    def __str__(self):
        return self.car_make + " " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_model = models.CharField(null=False, max_length=30, default='Car_Model')
    description = models.CharField(max_length=500)
    # Create a toString method for object string representation
    def __str__(self):
        return self.car_model + " " + self.description

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealership
        self.dealership = dealership
        # Name
        self.full_name = full_name
        # Purchase
        self.puchase = puchase
        # Review
        self.review = review
        # Purchase Date
        self.purchase_data = purchase_date
        # Car Make
        self.make = make
        # Car Model
        self.mode = model
        # Car Year
        self.caryear = caryear
        # Sentiment
        self.sentiment = sentiment
         # id
        self.id = id
    def __str__(self):
        return "Dealer name: " + self.full_name