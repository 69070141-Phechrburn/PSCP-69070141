"""ปราสาท"""
import math
def main():
    """castle tongkraduey"""
    N = int(input())
    if N == 1:
        print(0)
    else:
        R = math.ceil(math.sqrt(N))
        C = N - (R - 1) ** 2
        if C % 2 == 1:
            print(2 * (R - 1))
        else:
            print(2 * (R - 1) - 1)

main()
