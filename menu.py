class MyRestaurantMenu:
    def __init__(self):
        self.menu_items = {}

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if restaurant_name not in self.menu_items:
            self.menu_items[restaurant_name] = {}
        if item_name in self.menu_items[restaurant_name]:
            return f"{item_name} already exists in the menu for {restaurant_name}."
        self.menu_items[restaurant_name][item_name] = {'description': description, 'price': price}
        return f"{item_name} added to the menu for {restaurant_name}."

    def get_menu(self, restaurant_name):
        if restaurant_name in self.menu_items:
            return self.menu_items[restaurant_name]
        else:
            return f"Menu not found for {restaurant_name}."

    def update_menu_item(self, restaurant_name, item_name, new_description, new_price):
        if restaurant_name in self.menu_items and item_name in self.menu_items[restaurant_name]:
            self.menu_items[restaurant_name][item_name]['description'] = new_description
            self.menu_items[restaurant_name][item_name]['price'] = new_price
            return f"{item_name} updated in the menu for {restaurant_name}."
        else:
            return f"{item_name} not found in the menu for {restaurant_name}."

    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name in self.menu_items and item_name in self.menu_items[restaurant_name]:
            del self.menu_items[restaurant_name][item_name]
            return f"{item_name} deleted from the menu for {restaurant_name}."
        else:
            return f"{item_name} not found in the menu for {restaurant_name}."

# Usage example:
my_menu = MyRestaurantMenu()
result = my_menu.add_menu_item("My Restaurant", "Dish1", "Delicious dish", 15.99)
print(result)
