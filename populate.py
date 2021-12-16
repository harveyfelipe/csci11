import user_ops as user
import order_ops as order
from decimal import Decimal

if __name__ == '__main__':
    user.create_user("aarchamb", "Adam Archambault", "aarchambault0@wikipedia.org")
    aarchamb_home   = {
        "area": "Marilag",
        "city": "",
    } 
    aarchamb_office = {
        "street": "6 Manitowish Place",
        "state": "Csongrád",
        "country": "Hungary"
    }
    user.add_address("aarchamb", "home", aarchamb_home)
    user.add_address("aarchamb", "office",aarchamb_office)
    
    
    shopping_cart1 = [
        {
            'product_name' : 'New Apple MacBook Pro',
            'price'        : Decimal('2018.42'),
            'quantity'     : 1,
            'status'       : 'FILLED'
        },
        {
            'product_name' : 'Nintendo Switch',
            'price'        : Decimal('368.95'),
            'quantity'     : 1,
            'status'       : 'FILLED'
        },
        {
            'product_name' : 'Seagate Portable 2TB External',
            'price'        : Decimal('59.95'),
            'quantity'     : 1,
            'status'       : 'FILLED'
        },
        {
            'date'         : '11-11-2021',
            'status'       : 'SHIPPED'
        }
        ]
    
    shopping_cart2 = [
        {
            'product_name' : 'New Apple MacBook Pro',
            'price'        : Decimal('2018.42'),
            'quantity'     : 1,
            'status'       : 'FILLED'
        },
        {
            'product_name' : 'Charmin Ultra Soft Cushiony Touch Toilet Paper',
            'price'        : Decimal('0.49'),
            'quantity'     : 10,
            'status'       : 'FILLED'
        },
        {
            'product_name' : 'The Legend of Zelda: Breath of the Wild',
            'price'        : Decimal('74.94'),
            'quantity'     : 1,
            'status'       : 'FILLED'
        },
        {
            'date'         : '11-12-2021',
            'status'       : 'PLACED'
        }
        ]
        
    shopping_cart3 = [
        {
            'product_name' : 'HyperX Fury 16GB',
            'price'        : Decimal('39.99'),
            'quantity'     : 2,
            'status'       : 'PENDING'
        },
        {
            'product_name' : 'Jenga Classic Game',
            'price'        : Decimal('19.99'),
            'quantity'     : 1,
            'status'       : 'PENDING'
        },
        {
            'product_name' : 'Tasha\'s Cauldron of Everything',
            'price'        : Decimal('49.95'),
            'quantity'     : 3,
            'status'       : 'FILLED'
        },
        {
            'date'         : '11-13-2021',
            'status'       : 'PENDING'
        },
        ]
        
    shopping_cart4 = [
        {
            'product_name' : 'HyperX Fury 16GB',
            'price'        : Decimal('39.99'),
            'quantity'     : 2,
            'status'       : 'PENDING'
        },
        {
            'product_name' : 'Jenga Classic Game',
            'price'        : Decimal('19.99'),
            'quantity'     : 1,
            'status'       : 'PENDING'
        },
        {
            'product_name' : 'Tasha\'s Cauldron of Everything',
            'price'        : Decimal('49.95'),
            'quantity'     : 3,
            'status'       : 'FILLED'
        },
        {
            'date'         : '11-13-2021',
            'status'       : 'PENDING'
        },
        ]
        
    order.checkout("aarchamb", "home", shopping_cart1, shopping_cart1[-1]['date'], shopping_cart1[-1]['status'])
    order.checkout("tgrimes1", "home", shopping_cart2, shopping_cart2[-1]['date'], shopping_cart2[-1]['status'])
    order.checkout("tgrimes1", "home", shopping_cart3, shopping_cart3[-1]['date'], shopping_cart3[-1]['status'])
    order.checkout("tgrimes1", "home", shopping_cart4, shopping_cart4[-1]['date'], shopping_cart4[-1]['status'])