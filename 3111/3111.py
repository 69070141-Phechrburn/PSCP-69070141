"""สหกรณ์โรงเรียน"""
def main():
    """sahakornmalueyhuehin"""
    is_member = input()
    n = int(input())
    total = 0
    for _ in range(n):
        price = float(input())
        total += price
    if is_member == 'Y':
        final_price = total * 0.95
    elif is_member == 'N' and total >= 500:
        final_price = total * 0.97
    else:
        final_price = total
    final_price += 0.000000001
    print(f"{final_price:.2f}")

main()
