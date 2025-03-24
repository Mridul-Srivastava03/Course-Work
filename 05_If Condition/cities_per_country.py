India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city = input("Enter your city name: ")

if city in India:
    print("Your country is India.")
elif city in USA:
    print("Your country is USA.")
elif city in UK:
    print("Your country is UK.")
else:
    print("This City is in Alternate dimension.")

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in India and city2 in India:
    print("Both cities are in India.")
elif city1 in USA and city2 in USA:
    print("Both cities are in USA.")
elif city1 in UK and city2 in UK:
    print("Both cities are in UK.")
else:
    print("They dont belong to the same country.")