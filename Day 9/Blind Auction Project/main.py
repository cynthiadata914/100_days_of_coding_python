# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

from art import logo
print(logo)


def the_highest_bidder(bidding_score):
    highest_bid = 0
    winner = ""
    for bid in bidding_score:
        bid_amount = bidding_score[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# TODO-4: Compare bids in dictionary
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    Price = int(input("How much would you like to bid? $"))
    bids[name] = Price
    more_bids = input("Are there more bidders? type 'yes' or 'no': ")
    if more_bids == 'no':
        continue_bidding = False
        the_highest_bidder(bids)
    elif more_bids == 'yes':
        print("\n" * 20)


