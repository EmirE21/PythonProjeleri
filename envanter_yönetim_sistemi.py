inventory = {}
def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {
            "price": float(price),
            "stock": int(stock)
        }
        print(f"Item '{item}' added successfully.")
def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        current_stock = inventory[item]["stock"]
        new_stock = current_stock + quantity
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")
def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]["stock"]
def sales_report(sales):
    total = 0.0
    for item, qty in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        if inventory[item]["stock"] < qty:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        inventory[item]["stock"] -= qty
        total += inventory[item]["price"] * qty
    return f"Total revenue: ${total:.2f}"