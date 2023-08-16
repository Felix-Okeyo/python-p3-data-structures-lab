spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# returns a list of strings with the names of each spicy food.


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# eturns a list of dictionaries where the heat level of the food is greater than 5.


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


('''get_spicy_food_by_cuisine()
Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.

get_spicy_food_by_cuisine(spicy_foods, "American")

{"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
get_spicy_food_by_cuisine(spicy_foods, "Thai")

{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}
''')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


(''' print_spiciest_foods()
Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:

Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

Try to use functions you've already written to solve this!

print_spiciest_foods(spicy_foods)

Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
 ''')


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food['heat_level']
            print(
                f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


(''' get_average_heat_level()
Define a function average_heat_level() that takes a list of spicy_foods and returns an integer representing the average heat level of all the spicy foods in the array. Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.

average_heat_level(spicy_foods)

6
 ''')


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food['heat_level']
    return total_heat_level // len(spicy_foods)


(''' create_spicy_food()
Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added. 
 ''')


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
