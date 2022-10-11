cart={"apple"}
print(type(cart))
cities = ("Nagpur", "Pune","Mumbai","Bangalore")
print(cities)
cities_with_codes = (100,"Nagpur",101,"Pune",102,"Mumbai",102,"Bangalore")
profile = ("Baig", 23, False, "M")

for city in cities:
    print(city)
print("last city of the cities", cities[-1])
print("2nd city of the cities",cities[1])
c1,c2,c3,c4 = cities
print(c1,c2,c3,c4)
print(cities.index("Mumbai"))
print(len(cities))
