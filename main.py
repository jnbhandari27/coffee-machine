def get_response():
    response = input("Welcome!👋\nWhat would you like?\n🟢 Espresso \n🟡 Latte\n🟣 Cappuccino\nEnter your desired option: ")
    return response


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    amount = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return amount


def get_report():
    for key in resources:
        print(key, ": ", resources[key][0], [key][1])


def resources_data(water, milk, coffee, option):
    if option == 1:
        if water < resources["Water"][0] and milk < resources["Milk"][0] and coffee < resources["Coffee"][0]:
            return True
        else:
            return False
    else:
        resources["Water"][0] = resources["Water"][0] - water
        resources["Milk"][0] = resources["Milk"][0] - milk
        resources["Coffee"][0] = resources["Coffee"][0] - coffee
        return 0


resources = {
    "Water": [200, "ml"],
    "Milk": [200, "ml"],
    "Coffee": [100, "g"],
    "Money": [2.5, "$"]
}
coffee_type = {
    "Espresso": {
        "Water": [75, "ml"],
        "Milk": [50, "ml"],
        "Coffee": [25, "g"],
        "Money": [1.5, "$"]
    },
    "Latte": {
        "Water": [100, "ml"],
        "Milk": [75, "ml"],
        "Coffee": [50, "g"],
        "Money": [1.75, "$"]
    },
    "Cappuccino": {
        "Water": [50, "ml"],
        "Milk": [100, "ml"],
        "Coffee": [75, "g"],
        "Money": [2, "$"]
    }
}
machine = True
user_response = None

while user_response != "off":

    user_response = get_response()

    if user_response == "report":
        get_report()
        continue
    if user_response == "off":
        break
    water_req = coffee_type[user_response]["Water"][0]
    milk_req = coffee_type[user_response]["Milk"][0]
    coffee_req = coffee_type[user_response]["Coffee"][0]

    if resources_data(water_req, milk_req, coffee_req, 1) is False:
        print("Sorry☹, not enough resources available.")
        continue

    money_inserted = insert_coins()
    price_of_coffee = coffee_type[user_response]["Money"][0]
    if money_inserted < price_of_coffee:
        print("Sorry🙁 that's not enough money. Money refunded. Please try again!")
    else:
        if money_inserted > price_of_coffee:
            print(f"Here is {round((money_inserted - price_of_coffee), 2)} $ in change.💰")
        print(f"Enjoy your {user_response}!☕")
        resources_data(water_req, milk_req, coffee_req, 2)
