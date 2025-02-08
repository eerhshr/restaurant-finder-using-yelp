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


def all_filters(cuisine, rating):
    restaurant_options = []
    f = open('sampleData.json')
    data = json.load(f)

    for restaurant in data['businesses']:
        matches_cuisine = False
        # matches_price = False
        matches_rating = False

        for categories in restaurant['categories']:
            category = categories['title']
            if category == cuisine:
                matches_cuisine = True

        if restaurant['rating'] >= float(rating):
                matches_rating = True
            
        # try:
        #     if restaurant['price'] == price:
        #         matches_price = True
        # except KeyError:
        #     pass

        
        if matches_cuisine and matches_rating:
            restaurant_options.append(restaurant['name'])

    print(restaurant_options)
    f.close();