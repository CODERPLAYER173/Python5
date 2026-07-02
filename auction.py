

name = input("Enter your name here-:\n").lower()
bidding_value = int(input("Enter your bid-:\n$"))
continue1 = input("Are there any other players yes or no").lower()
bids = {}


def find():
    highest_bid = max(bids.values())
    highest_bidder = max(bids, key=bids.get)
    print(highest_bidder+" won with "+str(highest_bid))
while continue1 == "yes":
    print(art.logo)
    name = input("Enter your name here-:\n").lower()
    bidding_value = int(input("Enter your bid-:\n$"))
    continue1 = input("Are there any other players yes or no").lower()
    bids[name] = bidding_value

while continue1 == "no":
    find()
    break
