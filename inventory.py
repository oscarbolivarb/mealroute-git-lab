INVENTORY = {
    "rice": 18,
    "beans": 6,
    "pasta": 9,
    "canned_tomatoes": 4,
}

def low_stock_items(threshold=8):
    return [item for item, qty in INVENTORY.items() if qty < threshold]

def needs_restock(item_name, threshold=8):
    return INVENTORY.get(item_name, 0) < threshold
