def python_food():
    text = "spam and eggs"
    width = 80
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += f"{arg}{sep}"
    width = 80
    left_margin = (width - len(text)) // 2
    return " " * left_margin + text


    # with open("centered.txt", mode='a+') as centered_file:

print(centre_text("hello world!"))
centre_text("Cruel, cruel world!", )
centre_text(1023)
centre_text("furst", "second", 3, 4, "spam", sep=': ')
centre_text("hellob")
