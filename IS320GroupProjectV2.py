# Global Variables
customers = {'customer1_id': 'customer1_pass', 'customer2_id': 'customer2_pass'}
managers = {'manager_id': 'manager_pass'}
products = {
    'RD001': {'name': 'Red Dress', 'unit_price': 5.0, 'stock': 100},
    'BS001': {'name': 'Blue Shoes', 'unit_price': 10.0, 'stock': 50},
    'BS002': {'name': 'Black Shirt', 'unit_price': 5.00, 'stock': 25},
    # Add more products as needed
}
orders = []
order_id_counter = 10001

# Functions
def login():
    # Implement login functionality
    user_id = input("Enter your ID: ")
    password = input("Enter your password: ")
    if user_id in customers and customers[user_id] == password:
        return 'customer', user_id
    elif user_id in managers and managers[user_id] == password:
        return 'manager', user_id
    else:
        print("Invalid ID or password.")
        return None, None

#get date 
import datetime
import random

def get_date():
    start = datetime.date(2022,1,1)
    end = datetime.date(2023,12,31)
    order_date = start + (end - start) * random.random()

    return order_date 

def customer_menu(customer_id):
    # Implement customer menu options: submit order, view order history, logout
    global orders
    while True:
        print("Customer Menu:")
        choice = input("1. Submit Order\n2. View Order History\n3. Logout\nChoose an option: ")
        if choice == '1':
            submit_order(customer_id)
        elif choice == '2':
            display_order_history(customer_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

# Manager menu function
def manager_menu(manager_id):
    while True:
        print("Manager Menu:")
        choice = input("1. View All Orders 2. Manager Order Summary 3. Edit Prices\n4. Order More Inventory, 5. Logout: ")
        if choice == '1':
            manager_view_orders()
        elif choice == '2':
            manager_order_summary()
        elif choice == '3':
            edit_prices()
        elif choice == '4':
            # Implement order more inventory functionality
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def manager_view_orders():
    global orders
    if not orders:
        print("No orders found.")
    else:
        print("All Orders from All Customers:")
        for order in orders:
            print(f"Order ID: {order['order_id']}, Customer ID: {order['customer_id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}")

def manager_order_summary():
    # Leave the implementation blank for now
    pass

def edit_prices():
    global products

    # Display available products and their current prices
    print("Available Products and Current Prices:")
    for product_id, info in products.items():
        print(f"{product_id}: {info['name']} - ${info['unit_price']:.2f}")

    # Get the product ID to edit
    product_id = input("Enter the product ID you want to edit: ").strip().upper()

    # Check if the entered product ID exists
    if product_id in products:
        # Get the new unit price 
        new_price = float(input("Enter the new unit price: "))

        # Update product unit price
        products[product_id]['unit_price'] = new_price

        print(f"Price for Product ID {product_id} updated to ${new_price:.2f}")
    else:
        print(f"Product ID {product_id} not found")

def submit_order(customer_id):
    global order_id_counter
    print("Available Products:")
    for product_id, info in products.items():
        print(f"{product_id}: {info['name']} - ${info['unit_price']:.2f} - Stock: {info['stock']}")
    product_id = input("Enter the product ID you want to order: ").strip().upper()
    if product_id in products:
        quantity = int(input("Enter the quantity you want to order: "))
        if quantity <= products[product_id]['stock']:
            order_id = order_id_counter
            order_id_counter += 1
            order = {
                'order_id': order_id,
                'customer_id': customer_id,
                'product_id': product_id,
                'quantity': quantity,
                'order_price': quantity * products[product_id]['unit_price']
            }
            orders.append(order)
            print("Order placed successfully!")
            products[product_id]['stock'] -= quantity
        else:
            print("Insufficient stock.")
    else:
        print("Invalid product ID.")

def display_order_history(customer_id):
    # Implement functionality to display order history for a customer
    pass

def view_all_orders(manager_id):
    # Implement functionality to view all orders for a manager
    pass

def reset():
    global orders
    orders.clear()  # Clearing all orders

# Main Program
def main():
    global order_id_counter
    quit_program = False
    while not quit_program:
        print("Main Menu:")
        print("1. Login")
        print("2. Quit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            user_type, user_id = login()
            if user_type == 'customer':
                customer_menu(user_id)
            elif user_type == 'manager':
                manager_menu(user_id)
            else:
                print("Invalid ID or password.")
        elif choice == '2':
            quit_program = True
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
