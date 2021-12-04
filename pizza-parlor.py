# This program accepts pizza orders from users and returns an itemized receipt

toppings_inventory = {
	'onions':10,
	'peppers': 3,
	'pepperoni': 5,
	'sausage':6,
	'mushrooms': 4,
	'spinach': 2,
	'pineapple': 0
}
prices = {
	'pan' : 4.99,
	'thin' : 4.99,
	'deep dish': 6.99,
	'onions': .40,
	'peppers': .40,
	'pepperoni': .75,
	'sausage':.80,
	'mushrooms': .30,
	'spinach': .50,
	'pineapple': .70
}
revenue = 0

# This function takes a user's order. It will get the type of crust the user wants and the toppings. 
# This function will also call the check_stock() function for a user order to make sure that the topping is available
def take_order():
	pizza_order = {}
	order_toppings = []

	crust = input("What type of crust would you like? Pan, Deep Dish, Thin ")
	crust = crust.lower()
	pizza_order['crust'] = crust
	print("\nWe have the following toppings: ")
	for topping in toppings_inventory.keys():
		print(topping.title())

	another = True
	while another:
		choice = input("Choose a topping or type 'done': ")
		if choice.lower() == 'done':
			another = False
		elif choice.lower() == 'exit':
			return 'exit'
		else:
			if check_inventory(choice):
				order_toppings.append(choice)
			else:
				print("Sorry we don't have " + choice.title() + " at the moment.")
	pizza_order['toppings'] = order_toppings

	return pizza_order



# Updates the inventory
# Need to copy dictionary to a new one and update those values so that comparisons can be made 
def update_inventory(order):
	toppings = order['toppings'][:]
	for topping in toppings:
		toppings_inventory[topping] -= 1
	

# Prints an the pricing for each items on the order and the total
def print_receipt(order):
	print("\nReboot Iowa Pizzeria Receipt")
	crust_price = prices[order['crust']]
	print("Crust: " + order['crust'].title() + "..." + str(crust_price))
	print("Toppings: ")
	toppings_price = 0
	for topping in order['toppings']:
		toppings_price += prices[topping]
		print("\t" + topping.title() + "..." + str(toppings_price))
	total = toppings_price + crust_price
	print("Your total:\t" + str(total))
	return total

# This function checks the toppings dictionary to make sure toppings are still available
def check_inventory(ingredient):
	if(ingredient in toppings_inventory and toppings_inventory[ingredient] > 0):
		return True
	else:
		return False

# prints the current toppings inventory
def print_inventory():
	for k,v in toppings_inventory.items():
		print(k + ": "+ str(v))

active = True
while(active):
	print("Welcome to The Reboot Iowa Pizzeria.")
	order = take_order()
	if order != 'exit':
		print("Building your pizza...")
		update_inventory(order)
		print("Your pizza is ready.\n")
		print("\n--------------------------------------------------")
		revenue += print_receipt(order)
		print("\n--------------------------------------------------")
	else:
		active = False
print("\n*************************")
print("\nInformation for staff: \nInventory List")
print_inventory()
print("\nCurrent Revenue:\n" + str(revenue))
