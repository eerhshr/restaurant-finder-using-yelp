# This is a sample Python script.
import process_restaurant
import restaurant_scrapper


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    location = input('Please enter a city and state:')
    restaurant_scrapper.get_data(location)
    print('Cuisines Available:')
    process_restaurant.get_available_cuisines()
    cuisine = input('Please enter a preferred cuisine:')
    rating = input('Please enter rating:')
    price = input('Please enter price:')
    process_restaurant.all_filters(cuisine, rating, price)