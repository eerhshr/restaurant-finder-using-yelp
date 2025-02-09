from flask import Flask, render_template, request
import process_restaurant
import restaurant_scrapper
import json

app = Flask(__name__)

@app.route("/restaurant", methods=["GET", "POST"])
def index():
    restaurants = []
    cuisines = []

    if request.method == "POST":
        location = request.form["location"]
        restaurant_scrapper.get_data(location)

        # cuisines = process_restaurant.get_available_cuisines()
        # cuisine = request.form.get("cuisine")
        rating = request.form.get("rating")
        price = request.form.get("price")

        if rating and price:
            restaurants = process_restaurant.all_filters(rating, price)

        # json_data = json.dumps(restaurants)
        # print(json_data);
    return render_template("index.html", restaurants=restaurants)

if __name__ == "__main__":
    app.run(debug=True)
