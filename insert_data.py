import peewee
import models

#test data users
def user_test_data():
    user_test_source = [
        {'username': 'Test', 'user_email': 'test@hotmail.com', 'user_street': 'teststraat', 'user_housenumber': 1, 'user_postalcode' : "1234AB", 'user_town' : 'Alkmaar', 'user_country' : "Nederland" },
        {'username': 'Test2', 'user_email': 'test2@hotmail.com', 'user_street': 'testlaan', 'user_housenumber' : 2, 'user_postalcode' : "1234BC", 'user_town' : 'Alkmaar', 'user_country' : "Nederland" },
        {'username': 'Test3', 'user_email': 'test3@hotmail.com', 'user_street': 'dorpstraat', 'user_housenumber' : 3, 'user_postalcode' : "1235BC", 'user_town' : 'Amsterdam', 'user_country' : "Nederland" },
        {'username': 'Test4', 'user_email': 'test4@hotmail.com', 'user_street': 'kerkstraat', 'user_housenumber' : 2, 'user_postalcode' : "1234BC", 'user_town' : 'Alkmaar', 'user_country' : "Nederland" },
        {'username': 'Test5', 'user_email': 'test5@hotmail.com', 'user_street': 'testlaan', 'user_housenumber' : 2, 'user_postalcode' : "1234BC", 'user_town' : 'Alkmaar', 'user_country' : "Nederland" }    
    ]
    
    #insert test data users
    for data_dict in user_test_source:
        models.User.create(**data_dict)

#test data billing
def billing_test_data():
    billing_test_source = [
        {'userid': '1', 'ideal': False, 'paypal': True},
        {'userid': '2', 'ideal': True, 'paypal': False},
        {'userid': '3', 'ideal': False, 'paypal': True},
        {'userid': '4', 'ideal': True, 'paypal': False},
        {'userid': '5', 'ideal': False, 'paypal': True},
        ]
    
    #insert test data users
    for data_dict in billing_test_source:
        models.Billing.create(**data_dict)


#test data products
def product_test_data():
    product_test_source = [
        {'productname': 'Cotton longsleeve' , 'product_tag': '2' ,'product_description': 'a long sleeved t-shirt', 'price_per_unit': 5.00, 'quantity': 4, 'product_owner': "1"},
        {'productname': 'Dark jeans' , 'product_tag': '1' ,'product_description': 'denim jeans', 'price_per_unit': 20.00, 'quantity': 6, 'product_owner': "2"},
        {'productname': 'denim jacket' , 'product_tag': '3' ,'product_description': 'dark denim jacket', 'price_per_unit': 15.00, 'quantity': 4, 'product_owner': "1"},
        {'productname': 'Trench coat' , 'product_tag': '3' ,'product_description': 'Taupe trech coat', 'price_per_unit': 120.00, 'quantity': 2, 'product_owner': "2"},
        {'productname': 'Sweater' , 'product_tag': '4' ,'product_description': 'hoodie', 'price_per_unit': 19.00, 'quantity': 7, 'product_owner': "1"}
    ]

    #insert test data products
    for data_dict in product_test_source:
        models.Product.create(**data_dict)

#test data tags/tuple, dus geen dubbele
def tags_test_data():
    tag_test_source = [
        {'product_tag': '1','tag_description':'trousers'},
        {'product_tag': '2','tag_description':'shirts'},
        {'product_tag': '3','tag_description':'jackets'},
        {'product_tag': '4','tag_description':'sweaters'},
    ]

    #insert test data tags
    for data_dict in tag_test_source:
        models.Tag.create(**data_dict)

def transaction_test_data():
    transaction_test_source = [
        {'userid': '1','purchased_product':'2','quantity': '1'},
        {'userid': '2','purchased_product':'4','quantity': '1'},
        {'userid': '4','purchased_product':'5','quantity': '1'},
    ]

    #insert test data transaction
    for data_dict in transaction_test_source:
        models.TransactionTrack.create(**data_dict)


#create test db
def create_test_data():
    user_test_data()
    product_test_data() 
    billing_test_data()  
    tags_test_data() 
    transaction_test_data()

#if __name__ == "__main__":
models.db.connect()
models.db.create_tables([models.User, models.Billing, models.Product, models.Tag, models.TransactionTrack])
create_test_data()
