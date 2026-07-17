import random

def calculate_score(hand):
    score = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card == 'Ace':
            score += 11
        else:
            score += int(card)
    return score


def play_game():
    base_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Ace']
    deck_of_cards = []

    for card in base_cards:
        deck_of_cards.append(card)
        deck_of_cards.append(card)
        deck_of_cards.append(card)
        deck_of_cards.append(card)

    random.shuffle(deck_of_cards)

    player_hand = [deck_of_cards.pop(), deck_of_cards.pop()]
    computer_hand = [deck_of_cards.pop(), deck_of_cards.pop()]

    print("\nთამაში დაიწყო!")

    # მოთამაშის სვლა
    while True:
        player_score = calculate_score(player_hand)
        print(f"თქვენი კარტები: {player_hand} | ქულა: {player_score}")

        if player_score > 21:
            print("თქვენ წააგეთ")
            return "computer"

        choice = input("აირჩიეთ: 'add'  or 'stop': ").strip().lower()

        if choice == 'add':
            player_hand.append(deck_of_cards.pop())
        elif choice == 'stop':
            break

    # კომპიუტერის სვლა
    print("\nკომპიუტერის სვლა")
    while calculate_score(computer_hand) < 17:
        computer_hand.append(deck_of_cards.pop())

    computer_score = calculate_score(computer_hand)
    print(f"კომპიუტერის კარტები: {computer_hand} | ქულა: {computer_score}")


    print("\nსაბოლოო შედეგი")
    if computer_score > 21:
        print("თქვენ მოიგეთ")
        return "player"
    elif player_score > computer_score:
        print("თქვენ მოიგეთ")
        return "player"
    elif computer_score > player_score:
        print("თქვენ წააგეთ")
        return "computer"
    else:
        print("ფრეა!")
        return "draw"

while True:
    result = play_game()
    if result != "draw":
        break


