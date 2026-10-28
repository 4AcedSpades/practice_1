products = [ 
    {"name": "Keyboard", "price": 45}, 
    {"name": "Monitor", "price": 180}, 
    {"name": "Mouse", "price": 25}, 
    {"name": "Headphones", "price": 75}, 
    {"name": "USB Drive", "price": 15}, 
    {"name": "Webcam", "price": 60} 
]

def lesser_price(item):
    return item.get("price") <= 50

less_than_50 = filter(lesser_price, products)

print(list(less_than_50))