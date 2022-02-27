shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy"
]

def shopping(items, payment='card', shop='local'):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart, payment, shop

return_data = shopping(shopping_items)
shoping_cart, payment, shop = return_data
print(shoping_cart, shop)
