import peewee
from peewee import *

db = peewee.SqliteDatabase("betsy.db")

# Models go here

""" products kunnen maar door 1 user bezit worden, dus de stock is maar van 1 product bezit door 1 user. 
Het is een soort marktplaats, user bezitten producten en users kopen producten van andere users."""

#create db
class Basemodel(Model):
    class Meta:
        database = db

#A user has a name, address data, and billing information.
class User(Basemodel):
    username = CharField(index = True, unique=True)#index voor users en unieke waarde
    user_street = TextField()
    user_housenumber = IntegerField()
    user_postalcode = CharField()
    user_town = CharField()
    user_country = CharField()

class Billing(Basemodel):
    userid = ForeignKeyField(User)
    ideal = BooleanField()
    paypal = BooleanField()

#The tags should not be duplicated.
class Tag(Basemodel):
    product_tag = CharField(unique=True)
    tag_description = CharField (unique=True)
    
#The products must have a name, a description, a price per unit, 
#and a quantity describing the amount in stock.   
class Product(Basemodel):
    productname = CharField()
    product_description = CharField ()
    price_per_unit = DecimalField(rounding = 2) #The price should be stored in a safe way; rounding errors should be impossible.
    quantity = IntegerField()
    product_tag = ForeignKeyField(Tag)
    product_owner = ForeignKeyField(User) # Each user must be able to own a number of products

class TransactionTrack(Basemodel): ## The transaction model must link a buyer with a purchased product and a quantity of purchased items
    userid = ForeignKeyField(User) # only users can purchase goods
    purchased_product = ForeignKeyField(Product)
    quantity = IntegerField()    

#staat niet in de opdracht
class Inventory(Product,TransactionTrack):
    pass

