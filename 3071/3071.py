"""IloveHEE"""
def main():
    """IloveHEE"""
    x = int(input())
    y = int(input())
    z = int(input())
    a = int(input())
    total = 0
    for i in range(x, y+1):
        if i % z == a:
            total += 1
    print(total)

main()
