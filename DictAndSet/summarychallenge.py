choice = "-"
while choice != "0":
    if choice in set("12345"):
        print(f"You chose {choice}")
    else:
        print("Please choose your option from the list below:")
        print("1:learn pything")
        print("2:Leanr Jacvea")
        print("3:Go swimming")
        print("4:Fuck bitches")
        print("5:Get money")
        print("0: exit")

    choice = input()