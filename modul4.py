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
        shopping_cart += item + ", "
    return shopping_cart.split('\n'), payment, shop

return_data = shopping(shopping_items)
shoping_cart, payment, shop = return_data
print(return_data)
