ef get_city_price(city):# Library for the city prices
    city_prices = {
        "Lisbon": 225,
        "London": 375,
        "Madrid": 265,
        "Milan": 245,
        "Paris": 285
    }

    if city in city_prices:
        return city_prices[city]
    else:
        return None

def calculate_total_nights_cost(num_nights): # Calculating the price for the inputted int of nights stayed
    return num_nights * 49

def calculate_total_rental_days_cost(rental_days): # Calculating the price for the inputted int of rental days stayed
    return rental_days * 28

def calculate_total_cost(city_price, total_num_nights, total_rental_days): # Calculating the total price of the holiday
    return city_price + total_num_nights + total_rental_days

def main(): # Asking user to input their destination of choice
    city_flight = input("Which city are you flying to? Choose from: Lisbon (£225), London (£375), Madrid (£265), Milan (£245), Paris (£285): ")

    city_price = get_city_price(city_flight)

    if city_price is not None: # Asking user to input the days they plan on renting a car and staying at an hotel
        num_nights = int(input("How many nights do you plan on staying? (£49 p/n): "))
        rental_days = int(input("How many days do you plan to rent a car? (£28 per day): "))

# calculation of inputs
        total_num_nights = calculate_total_nights_cost(num_nights)
        total_rental_days = calculate_total_rental_days_cost(rental_days)

        total_cost = calculate_total_cost(city_price, total_num_nights, total_rental_days)
#printing of variables and total holiday
        print(f"The cost of your flight is £{city_price}, hotel stay £{total_num_nights} and car rental {total_rental_days}")
        print(f"Therefore, the total cost of your holiday to {city_flight} is £{total_cost}")
    else:
        print("Invalid city")

# Check if the script is executed as the main module
if __name__ == "__main__":
    # Call the main function (if needed)
    git_task_project()