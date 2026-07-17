import random
import logging

logging.basicConfig(
    filename='lottery_logs',
    level=logging.INFO
)

jackpot_amount = 1000000

winning_numbers = random.sample(range(1, 49), 6)

player_numbers = []

print("შეიყვანოთ 6 განსხვავებული რიცხვი 1-დან 49-მდე:")

for x in range(1, 7):
    number = int(input(f"შეიყვანეთ მე-{x} რიცხვი: "))
    player_numbers.append(number)

matches = 0
for num in player_numbers:
    if num in winning_numbers:
        matches += 1

winning_amount = 0
result_message = ""

if matches == 6:
    winning_amount = jackpot_amount
    result_message = "თქვენ მოიგეთ JACKPOT!"
elif matches == 5:
    winning_amount = jackpot_amount * 0.60
    result_message = f"თქვენ გამოიცანით 5 რიცხვი! მოიგეთ — {winning_amount} ლარი!"
elif matches == 4:
    winning_amount = jackpot_amount * 0.40
    result_message = f"თქვენ გამოიცანით 4 რიცხვი! მოიგეთ — {winning_amount} ლარი!"
elif matches == 3:
    winning_amount = jackpot_amount * 0.20
    result_message = f"თქვენ გამოიცანით 3 რიცხვი! მოიგეთ — {winning_amount} ლარი!"
else:
    winning_amount = 0
    result_message = "სამწუხაროდ, თქვენ დამარცხდით."

print("\nგათამაშების შედეგები")
print(f"მომგებიანი რიცხვები იყო: {winning_numbers}")
print(f"თქვენი რიცხვებია: {player_numbers}")
print(f"დამთხვევების რაოდენობა: {matches}")
print(f"შედეგი: {result_message}")
if winning_amount > 0:
    print(f"თქვენი მოგებული თანხაა: {winning_amount} ლარი!")

log_text = (
    f"გათამაშება: მომგებიანი: {winning_numbers} | "
    f"მოთამაშის: {player_numbers} | "
    f"დამთხვევა: {matches} | "
    f"მოგება: {winning_amount} ლარი"
)
logging.info(log_text)
