import random

# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

# deal the cards 
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand
def total(turn):
    total = 0 
    for card in turn:
        if isinstance(card, int):
            total += card 
        elif card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            total += 11 if total <= 10 else 1
    return total
    

# check for winner
def revealdealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# Add player name input and welcome message
playerName = input("Enter your name: ")
print(f"Welcome to Blackjack, {playerName}!")

while True:
    # Reset deck and hands for each game
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    playerHand = []
    dealerHand = []
    playerIn = True
    dealerIn = True

    # deal the cards 
    for _ in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)

    # Player's turn
    while playerIn:
        print(f"Dealer had {revealdealerHand()} and X")
        print(f"{playerName}, you have {playerHand} for a total of {total(playerHand)}")
        if total(playerHand) == 21:
            print(f"{playerName}, you have 21! Standing automatically.")
            playerIn = False
            break
        standOrHit = input("1: Stand\n2: Hit\n")
        if standOrHit == '2':
            dealCard(playerHand)
            if total(playerHand) >= 21:
                break
        else:
            playerIn = False

    # Dealer's turn
    while dealerIn and total(playerHand) <= 21:
        if total(dealerHand) < 17:
            dealCard(dealerHand)
        else:
            dealerIn = False
        if total(dealerHand) >= 21:
            break

    # Show dealer's full hand before results
    print(f"\nDealer's hand: {dealerHand} for a total of {total(dealerHand)}")

    # Results
    if total(playerHand) == 21:
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack You win!")
    elif total(dealerHand) == 21:
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack Dealer wins!")
    elif total(playerHand) > 21:
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You busted! Dealer wins!")
    elif total(dealerHand) > 21:
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer busted! You win!")
    elif total(playerHand) == total(dealerHand):
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Push! It's a tie.")
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer wins!")
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(f"\n{playerName}, you have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You win!")

    # Play again prompt
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break