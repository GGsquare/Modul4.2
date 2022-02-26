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
    pass
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

basket = shopping(shopping_items)
print(basket)