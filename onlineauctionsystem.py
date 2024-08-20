# Auction System Code in Python

class Auction:
    def __init__(self, item_name, start_price):
        self.item_name = item_name
        self.start_price = start_price
        self.current_price = start_price
        self.bidders = {}

    def place_bid(self, bidder_name, bid_amount):
        if bid_amount > self.current_price:
            self.current_price = bid_amount
            self.bidders[bidder_name] = bid_amount
            print(f"{bidder_name} has placed a bid of ${bid_amount} on {self.item_name}")
        else:
            print("Bid amount is too low. Please try again.")

    def get_current_price(self):
        return self.current_price

    def get_bidders(self):
        return self.bidders

    def close_auction(self):
        if len(self.bidders) > 0:
            winner = max(self.bidders, key=self.bidders.get)
            print(f"The auction for {self.item_name} has ended. The winner is {winner} with a bid of ${self.bidders[winner]}")
        else:
            print(f"The auction for {self.item_name} has ended with no bids.")

class AuctionHouse:
    def __init__(self):
        self.auctions = {}

    def create_auction(self, item_name, start_price):
        auction = Auction(item_name, start_price)
        self.auctions[item_name] = auction
        print(f"Auction created for {item_name} with a starting price of ${start_price}")

    def get_auction(self, item_name):
        return self.auctions.get(item_name)

    def list_auctions(self):
        for item_name, auction in self.auctions.items():
            print(f"{item_name}: ${auction.get_current_price()}")

def main():
    auction_house = AuctionHouse()

    while True:
        print("Auction House Menu:")
        print("1. Create Auction")
        print("2. List Auctions")
        print("3. Place Bid")
        print("4. Close Auction")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            start_price = float(input("Enter starting price: "))
            auction_house.create_auction(item_name, start_price)

        elif choice == "2":
            auction_house.list_auctions()

        elif choice == "3":
            item_name = input("Enter item name: ")
            auction = auction_house.get_auction(item_name)
            if auction:
                bidder_name = input("Enter your name: ")
                bid_amount = float(input("Enter your bid amount: "))
                auction.place_bid(bidder_name, bid_amount)
            else:
                print("Auction not found.")

        elif choice == "4":
            item_name = input("Enter item name: ")
            auction = auction_house.get_auction(item_name)
            if auction:
                auction.close_auction()
            else:
                print("Auction not found.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()