from deep_copy_challenge import deep_copy_dict
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy1 = copy.deepcopy((original))
copy2 = deep_copy_dict(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1] .append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")
print(id(original), original)
print(id(copy1), copy1)
print(id(copy2), copy2)
