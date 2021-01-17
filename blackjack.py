import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dealcard():
    card =random.choice(cards)
    return card
user_cards = []
computer_cards = []
for i in range(0,2):
    card=dealcard()
    user_cards.append(card)
for i in range(0,2):
    card=dealcard()
    computer_cards.append(card)
print(f"Your cards are {user_cards}")
print(f"Opponent's cards are {computer_cards}")
def calculate_score(cards):
    total_sum =sum(cards)
    return total_sum
def blackjack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
blackjack_comp =blackjack(computer_cards)
blackjack_user =blackjack(user_cards)
    
user_total =calculate_score(user_cards)
comp_total =calculate_score(computer_cards)
if user_total>21:
    for i in user_cards:
        if i==11:
            user_total-=10
if comp_total>21:
    for i in comp_total:
        if i==11:
            comp_total-=10            
if user_total<21:
    ans =input("Do you want another card? Type y or n\n")
    if ans =="y":
        card=dealcard()
        print(f"New card is {card}")
        user_cards.append(card)
        user_total =calculate_score(user_cards)
    elif comp_total<17:
        card=dealcard()
        computer_cards.append(card)
        comp_total =calculate_score(computer_cards)
if blackjack_comp ==0:
    print("You Lose")
if blackjack_user ==0:
    print("You Win")    
if comp_total>21:
    print("You Win")
if comp_total>user_total:
    print("You Lose")
elif user_total>comp_total:
    print("You Win")
elif user_total==comp_total:
    print("Its a Tie")   
else:
    print("Error,Try Again!!")   
print(f"   Your final hand: {user_cards}, final score: {user_total}")
print(f"   Computer's final hand: {computer_cards}, final score: {comp_total}")              
                






                