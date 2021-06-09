def deep_copy_dict(d: dict):
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


dict1 = {
    "Emily": ["niece", 9],
    "Oliver": ["nephew", 5],
    "Selina": ["demon", 2],
}

dict1_copy = deep_copy_dict(dict1)
dict1_copy["Selina"] = [5]

print(dict1["Selina"])
print(dict1_copy["Selina"])
