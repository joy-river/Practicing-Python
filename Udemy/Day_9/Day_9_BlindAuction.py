from BlindAuction_art import logo
import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


clearConsole()
bids = {}
repeat = "yes"
max_bid = 0
max_bidder = ""

print(logo)
print("Welcome to the secret auction program.")

while (repeat == "yes"):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))

    if (bid > max_bid):
        max_bid = bid
        max_bidder = name

    repeat = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    clearConsole()

print(f"{max_bidder} is win in {max_bid}$ !")
