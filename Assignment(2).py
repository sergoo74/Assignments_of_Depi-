#1
products = [
    ("Laptop", 1200, 5),
    ("Smartphone", 700, 10),
    ("Headphones", 150, 15),
    ("Monitor", 300, 7)
]
threshold = 500
above_threshold=[product[0] for product in products if product[1]> threshold]

print(f"Products above the price threshold:{above_threshold}") #Products above the price threshold
#2
salaries = {
    101: 50000,
    102: 60000,
    103: 55000
}
increments = [
    (101, 10),  # 10% increment
    (104, 5),   # 5% increment, not in salaries
    (102, 15)
]
for employer,increment in increments:
    if employer in salaries:
        salaries[employer] +=salaries[employer] *(increment/100)
print(f"Updated salaries: {salaries}") #Updated salaries

