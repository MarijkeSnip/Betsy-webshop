from models import *
import peewee
from textblob import Word


__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


"""Search for products based on a term. Searching for 'sweater' should yield all products that have 
the word 'sweater' in the name. This search should be case-insensitive. 
The search should target both the name and description fields.
Finally the search should account for spelling mistakes made by users and return products even if a spelling 
error is present
- productname
- product_description
- tag_description"""
def search(term):
    term = term.lower()
    search_word = Word(term)
    result = search_word.correct()

    search_results = []
    query_result = (Product.select().join(Tag).where(Product.productname.contains(result) | Product.product_description.contains(result) | Tag.tag_description.contains(result)))
    query_term = (Product.select().join(Tag).where(Product.productname.contains(term) | Product.product_description.contains(term) | Tag.tag_description.contains(term)))

    for product in query_term:
        if product.productname not in search_results:
            search_results.append(product.productname)

    if not search_results: #als term niets oplevert zoeken op aangepaste term
        for product in query_result:
            if product.productname not in search_results:
                search_results.append(product.productname)
    
    if search_results:
        print(search_results)
    else:
        print(f'There are no search results for {term}')
                

#View the products of a given user.
def list_user_products(user_id):
    user_products = []
    query = Product.select().where(Product.product_owner == user_id)

    for product in query:
        if product.productname not in user_products:
            user_products.append(product.productname)
    print(user_products)
    return user_products


#View all products for a given tag.
def list_products_per_tag(tag_id):
    products_tag = []
    query = Product.select().where(Product.product_tag == tag_id)

    for product in query:
        if product.productname not in products_tag:
            products_tag.append(product.productname)
        print(products_tag)
        return product.productname
    

#Add a product to a user.
def add_product_to_catalog(user_id, productname, description, price, quantity, tag):
    query = Product.create(productname = productname, product_description = description, 
    price_per_unit = price, quantity = quantity, product_tag = tag, product_owner = user_id)

    print(f'{quantity} x {productname} is added')  

#Remove a product from a user.
def remove_product(product_id):
    query = Product.delete().where(Product.id == product_id)
    query.execute()
     

#Update the stock quantity of a product.
def update_stock(product_id, new_quantity):
    query=Product.update({Product.quantity:new_quantity}).where(Product.id == product_id)
    query.execute()

#Handle a purchase between a buyer and a seller for a given product
#add transaction, update stock
def purchase_product(product_id, buyer_id, quantity):
    #update transanction
    add_transaction = TransactionTrack.create(purchased_product = product_id, userid = buyer_id, quantity = quantity)

    #update current quantity
    query = Product.select(Product.quantity).where(Product.id == product_id)
   
    for n in query:
        current_stock = n.quantity
    
    update_quantity = current_stock - quantity

    update_stock(product_id = product_id, new_quantity = update_quantity)
    


if __name__ == "__main__":
    search()
    list_user_products()
    list_products_per_tag()
    add_product_to_catalog()
    remove_product()
    update_stock()
    purchase_product()
