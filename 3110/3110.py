"""IloveHEE"""
def main():
    """IloveHEE"""
    travel = input()
    weight = float(input())
    split_trv = travel.split()
    if split_trv[0] == "BKK" and split_trv[1] == "CNX":
        print(f"{10 + weight * 30:.2f}")
    elif split_trv[0] == "BKK" and split_trv[1] == "PKT":
        print(f"{25 + weight * 50:.2f}")
    elif split_trv[0] == "CNX" and split_trv[1] == "UBP":
        print(f"{15 + weight * 40:.2f}")
    elif split_trv[0] == "UBP" and split_trv[1] == "BKK":
        print(f"{20 + weight * 40:.2f}")
    elif split_trv[0] == "PKT" and split_trv[1] == "CNX":
        print(f"{30 + weight * 60:.2f}")
    elif split_trv[0] == "UBP" and split_trv[1] == "PKT":
        print(f"{40 + weight * 70:.2f}")
    else:
        print("Error")

main()
