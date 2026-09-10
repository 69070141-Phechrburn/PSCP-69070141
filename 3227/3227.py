"""deck of cards"""
def main():
    """deck of cards"""
    card = input().strip().upper()
    rank_code, suit_code = card[:-1], card[-1]
    ranks = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
    suits = {"D": "diamonds", "H": "hearts", "S": "spades", "C": "clubs"}
    rank_str = ranks.get(rank_code, rank_code)
    suit_str = suits.get(suit_code, "")
    print(f"{rank_str} of {suit_str}".lower())

main()
