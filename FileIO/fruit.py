import shelve

with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit grown in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit['lime'] = "great with tequila"

for snack in fruit:
    print(f"{snack} : {fruit[snack]}")

while True:
    shelf_key = input("Please enter a fruit \n> ")
    if shelf_key == "quit":
        break
    if shelf_key in fruit:
        description = fruit.get(shelf_key)
        print(description)
    else:
        print(f"We don't have any {shelf_key}")

ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f"{f} - {fruit[f]}")

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)
print(fruit.items())

fruit.close()


