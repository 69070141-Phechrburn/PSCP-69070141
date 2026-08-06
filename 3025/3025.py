"""season"""
def main():
    """season"""
    months = int(input())
    days = int(input())
    if (months == 12 and days >= 21) or (1 <= months <= 2) or (months == 3 and days < 21):
        print("winter")
    elif (months == 3 and days >= 21) or (4 <= months <= 5) or (months == 6 and days < 21):
        print("spring")
    elif (months == 6 and days >= 21) or (7 <= months <= 8) or (months == 9 and days < 21):
        print("summer")
    elif (months == 9 and days >= 21) or (10 <= months <= 11) or (months == 12 and days < 21):
        print("fall")

main()
