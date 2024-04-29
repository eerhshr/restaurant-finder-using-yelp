import json


def get_available_cuisines():
    cuisines = []
    f = open('sampleData.json')
    data = json.load(f)

    for restaurant in data['businesses']:
        for categories in restaurant['categories']:
            cuisines.append(categories['title'])

    print(set(cuisines))

    f.close();


def filter_by_cuisine(cuisine):
    restaurants = []
    f = open('sampleData.json')
    data = json.load(f)

    for restaurant in data['businesses']:
        for categories in restaurant['categories']:
            category = categories['title']
            if category == cuisine:
                restaurants.append(restaurant['name'])

    print(restaurants)
    f.close();


def filter_by_rating(rating):
    f = open('sampleData.json')
    data = json.load(f)

    for restaurant in data['businesses']:
        if restaurant['rating'] >= float(rating):
            print(restaurant['name'])

    f.close();


def filter_by_price(price_pref):
    restaurant_options = []

    f = open('sampleData.json')
    data = json.load(f)

    for restaurant in data['businesses']:
        try:
            if restaurant['price'] and restaurant['price'] == price_pref:
                restaurant_options.append(restaurant['name'])
        except KeyError:
            pass

    print(restaurant_options)
    f.close()


def all_filters(cuisine, rating, price):
    restaurant_options = []
    f = open('sampleData.json')
    data = json.load(f)

    for restaurant in data['businesses']:
        for categories in restaurant['categories']:
            category = categories['title']
            try:
                if category == cuisine and restaurant['rating'] >= float(rating) and restaurant['price'] == price:
                    restaurant_options.append(restaurant['name'])
            except KeyError:
                pass

    print(restaurant_options)
    f.close();