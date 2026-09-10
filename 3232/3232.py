"""frog kradoon"""
def main():
    """frog kradoon"""
    x, y = map(int, input().split())
    total_distance = 0
    jumps = 0
    while total_distance < y:
        if x <= 0:
            jumps = -1
            break
        total_distance += x
        jumps += 1
        x -= 2

    print(jumps)

main()
