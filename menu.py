# menu.py

class Menu:
    def __init__(self):
        self.menu_data = {}

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if restaurant_name not in self.menu_data:
            raise ValueError(f"Restaurant '{restaurant_name}' not found.")
        
        if item_name in self.menu_data[restaurant_name]:
            raise ValueError(f"Menu item '{item_name}' already exists for '{restaurant_name}'.")
        
        self.menu_data[restaurant_name][item_name] = {'description': description, 'price': price}
        return f"Menu item '{item_name}' added to '{restaurant_name}'."

    def get_menu(self, restaurant_name):
        if restaurant_name not in self.menu_data:
            raise ValueError(f"Restaurant '{restaurant_name}' not found.")
        
        return self.menu_data[restaurant_name]

    def update_menu_item(self, restaurant_name, item_name, new_description, new_price):
        if restaurant_name not in self.menu_data or item_name not in self.menu_data[restaurant_name]:
            raise ValueError(f"Menu item '{item_name}' not found for '{restaurant_name}'.")
        
        self.menu_data[restaurant_name][item_name]['description'] = new_description
        self.menu_data[restaurant_name][item_name]['price'] = new_price
        return f"Menu item '{item_name}' updated for '{restaurant_name}'."

    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name not in self.menu_data or item_name not in self.menu_data[restaurant_name]:
            raise ValueError(f"Menu item '{item_name}' not found for '{restaurant_name}'.")
        
        del self.menu_data[restaurant_name][item_name]
        return f"Menu item '{item_name}' deleted from '{restaurant_name}'."


# conftest.py

import pytest
from menu import Menu

@pytest.fixture
def sample_menu():
    menu = Menu()
    menu.menu_data = {
        'RestaurantA': {
            'Item1': {'description': 'Description1', 'price': 10.99},
            'Item2': {'description': 'Description2', 'price': 15.99}
        },
        'RestaurantB': {}
    }
    return menu


# test_menu.py

import pytest
from menu import Menu

def test_add_menu_item(sample_menu):
    # Positive test case
    result = sample_menu.add_menu_item('RestaurantB', 'NewItem', 'New Description', 12.99)
    assert result == "Menu item 'NewItem' added to 'RestaurantB'."

    # Edge case: Adding a menu item to a non-existent restaurant
    with pytest.raises(ValueError, match="Restaurant 'NonExistentRestaurant' not found."):
        sample_menu.add_menu_item('NonExistentRestaurant', 'NewItem', 'New Description', 12.99)

    # Edge case: Adding a duplicate menu item
    with pytest.raises(ValueError, match="Menu item 'Item1' already exists for 'RestaurantA'."):
        sample_menu.add_menu_item('RestaurantA', 'Item1', 'Duplicate Description', 20.99)

    # Edge case: Adding a menu item with an invalid price
    with pytest.raises(ValueError, match="Invalid price value."):
        sample_menu.add_menu_item('RestaurantB', 'InvalidItem', 'Invalid Description', -5.99)

def test_get_menu(sample_menu):
    # Positive test case
    result = sample_menu.get_menu('RestaurantA')
    assert result == {'Item1': {'description': 'Description1', 'price': 10.99},
                      'Item2': {'description': 'Description2', 'price': 15.99}}

    # Edge case: Retrieving a menu from a non-existent restaurant
    with pytest.raises(ValueError, match="Restaurant 'NonExistentRestaurant' not found."):
        sample_menu.get_menu('NonExistentRestaurant')

def test_update_menu_item(sample_menu):
    # Positive test case
    result = sample_menu.update_menu_item('RestaurantA', 'Item1', 'Updated Description', 18.99)
    assert result == "Menu item 'Item1' updated for 'RestaurantA'."

    # Edge case: Updating a non-existent menu item
    with pytest.raises(ValueError, match="Menu item 'NonExistentItem' not found for 'RestaurantA'."):
        sample_menu.update_menu_item('RestaurantA', 'NonExistentItem', 'New Description', 25.99)

    # Edge case: Updating a menu item with invalid data
    with pytest.raises(ValueError, match="Invalid price value."):
        sample_menu.update_menu_item('RestaurantA', 'Item2', 'Updated Description', -8.99)

def test_delete_menu_item(sample_menu):
    # Positive test case
    result = sample_menu.delete_menu_item('RestaurantA', 'Item1')
    assert result == "Menu item 'Item1' deleted from 'RestaurantA'."

    # Edge case: Deleting a non-existent menu item
    with pytest.raises(ValueError, match="Menu item 'NonExistentItem' not found for 'RestaurantA'."):
        sample_menu.delete_menu_item('RestaurantA', 'NonExistentItem')

    # Edge case: Deleting a menu item from a non-existent restaurant
    with pytest.raises(ValueError, match="Restaurant 'NonExistentRestaurant' not found."):
        sample_menu.delete_menu_item('NonExistentRestaurant', 'Item2')
