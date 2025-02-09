import process_restaurant
import restaurant_scrapper

def print_hi(name):
    print(f'Hi, {name}') 

if __name__ == '__main__':
    location = input('Please enter a city and state:')
    restaurant_scrapper.get_data(location)
    print('Cuisines Available:')
    process_restaurant.get_available_cuisines()
    cuisine = input('Please enter a preferred cuisine:')
    rating = input('Please enter rating:')
    price = input('Please enter price:')
    process_restaurant.all_filters(cuisine, rating, price )