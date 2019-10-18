sneakers = {'name': ‘Fire Jordan', 'price': 800} B &

def discount_price(product, discount):
newPrice = int(product['price'] * (1.@ - discount) )
assert (@ <= newPrice <= product['price']), "Discount price is lower than zero"

igch UT mall os ely

50% 0
print(discount_price(sneakers, 0.5))
7 ag
print(discount_price(sneakers, 2))