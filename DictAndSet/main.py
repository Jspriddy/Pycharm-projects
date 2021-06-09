import copy

animals = {
    "lion": ["big", "scary", "fierce"],
    "tigers": ["cuddly", "soft", "tender"],
    "bears": ["oh my!"]
}
# Perform a shallow copy
# things = animals.copy()

things = copy.deepcopy(animals)

things["lion"].append("meow")

print(animals["lion"])
print(things["lion"])

print(id(animals["lion"]), animals["lion"])
print(id(things["lion"]), things["lion"])