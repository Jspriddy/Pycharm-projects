def parabola(x):
    y = x * x
    return y


last_x = 0
y2 = 0
negative_nums = []
negative = {}
for x in reversed(range(-100, )):
    y = parabola(x)
    y_diff = x + last_x
    if x == -1:
        result = f"{x}: {y}"
    else:
        result = f"x = {x} | y = {y} | y increased by {abs(y_diff)} | {abs(x)} + {abs(last_x)} = {abs(y_diff)}"
    negative_nums.append(result)
    negative[x] = y
    y2 = parabola(x)
    last_x = x

negative_nums.reverse()
for i in negative_nums:
    print(i)


negative

for x, y in reversed(negative.items()):
    print(f"{x}: {y}")





# for x in range(101):
#     y = parabola(x)
#     y_diff = x + last_x
#
#     if x in range(-1, 2):
#         print(f"{x}: {y}")
#     if x > 1:
#         print(f"x = {x} | y = {y} | y increased by {abs(y_diff)} | {abs(x)} + {abs(last_x)} = {abs(y_diff)}")
#     y2 = parabola(x)
#     last_x = x
