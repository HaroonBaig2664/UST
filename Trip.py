	
def hotel_cost(nights):
    return 140*nights
	
def plane_ride_cost(city):
 string = input("Enter the City :")
if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    else "Los Angeles" == city:
        return 475
		
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
    
def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)

		
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
	

