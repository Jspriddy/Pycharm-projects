jabber = open("/home/jonathan/Downloads/sample.txt", 'r')

for line in jabber:
    print(line, end='')

jabber.close()

# with closes the file

# with open("/home/jonathan/Downloads/sample.txt") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
# with open("/home/jonathan/Downloads/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
#
# for line in lines:
#     print(line, end='')
#

# Reads one line and prints it as str
with open("/home/jonathan/Downloads/sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

# Reads all lines, appends them to a list, and then prints by iterating through the list
# end='' removes /n from each item in the list
with open("/home/jonathan/Downloads/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
    print(lines)

for line in lines[::-1]:
    print(line, end='')

# reads the file as an individual string
with open("/home/jonathan/Downloads/sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')