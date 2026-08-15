"""bridge"""
def main():
    """bridge"""
    small = int(input())
    big = int(input())
    lick = int(input())
    if not lick%5 and big >= (lick // 5):
        print("0")
    elif small >= (lick % 5) and big >= (lick // 5):
        print(lick % 5)
    elif big < (lick // 5) and small >= (lick - big*5):
        print(lick - big*5)
    else:
        print(-1)

main()
