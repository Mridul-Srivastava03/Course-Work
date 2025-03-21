indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print(f"{dish} is Indian Cuisine.")
elif dish in chinese:
    print(f"{dish} is Chinese Cuisine.")
elif dish in italian:
    print(f"{dish} is Italian Cuisine.")
else:
    print("I dont know which cuisine is this!")