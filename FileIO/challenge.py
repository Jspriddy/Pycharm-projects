# append the times table to our jabberwocky poem

# the first column of numbers should be right justified
nieces = ["Emily", "Oliver", "Sophie", "Selina"]

with open("sample2.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print(f"{i} times {j} is {i * j}", file=tables)
        print("-" * 20, file=tables)

with open("newfile.txt", 'w+') as entries:
    for niece in nieces:
        print(f"{niece} is my favorite niece", end='\n', file=entries)

with open("newfile.txt", 'r') as entries:
    lines = entries.readlines()

for line in lines:
    print(line, end='')
