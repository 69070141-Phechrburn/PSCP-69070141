"""IloveHEE"""
def main():
    """IloveHEE"""
    total = float(input())
    maximun_outburtscumming = float(input())
    remains = total - 2*(maximun_outburtscumming)
    if remains < 0:
        remains = 0
    if maximun_outburtscumming  - remains > 2:
        print("Surprising")
    else:
        print("Not surprising")
    #kuylek

main()
