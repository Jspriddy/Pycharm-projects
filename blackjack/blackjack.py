import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
        disable_buttons()
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
        disable_buttons()
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        disable_buttons()
    else:
        result_text.set("Draw!")
        disable_buttons()


def disable_buttons():
    dealer_button.configure(state="disabled")
    player_button.configure(state="disabled")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Busted!\nDealer wins!")
        disable_buttons()
    if player_score == 21:
        result_text.set("Blackjack! Player wins!")
        disable_buttons()


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    # calculate the score of all cards in the list
    # only one ace can have the value 11 and this will be reduced to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        second_ace = False
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def load_images(card_images):
    suits = ['heart', 'diamond', 'club', 'spade']
    face_cards = ['jack', 'queen', 'king']
    file_type = 'png'

    decks = 0
    while decks < 3:
        for suit in suits:
            for card in range(1, 11):
                name = 'cards/{}_{}.{}'.format(str(card), suit, file_type)
                image = tkinter.PhotoImage(file=name)
                card_images.append((card, image,))
            for card in face_cards:
                name = 'cards/{}_{}.{}'.format(card, suit, file_type)
                image = tkinter.PhotoImage(file=name)
                card_images.append((10, image))
        decks += 1


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    shuffle()
    # embedded frame to hold card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    dealer_button.configure(state="normal")
    player_button.configure(state="normal")

    result_text.set("")

    dealer_hand = []
    player_hand = []
    play()


def shuffle():
    global deck
    deck = list(cards)
    random.shuffle(deck)


def play():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

    mainWindow.mainloop()


mainWindow = tkinter.Tk()

mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text, background="green")
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0, padx=10)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0,
                                                                                                padx=10)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0, padx=10)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0,
                                                                                                padx=10)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow, background="green")
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

player_button = tkinter.Button(button_frame, text="Hit", command=deal_player)
player_button.grid(row=0, column=0, padx=10, pady=10)

dealer_button = tkinter.Button(button_frame, text="Stay", command=deal_dealer)
dealer_button.grid(row=0, column=1, padx=10)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2, padx=10)

cards = []
load_images(cards)
deck = list(cards)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()















