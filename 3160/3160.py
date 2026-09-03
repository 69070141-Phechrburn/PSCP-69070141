"""lekkchaprohathummhai"""
def main():
    """lekkchaprohathummhai"""
    lekk = input().split(" ")
    lekkloop_f = int(lekk[0])
    lekkloop_s = int(lekk[1])
    prime = []
    prime_n = 0
    for a in range(lekkloop_f, lekkloop_s + 1):
        if a <= 1:
            continue
        for i in range(2, a):
            if not a % i:
                break
        else:
            prime.append(a)
            prime_n += 1
    if prime:
        print(*prime)
        print(f"Total primes: {prime_n}")
    else:
        print(f"Total primes: {prime_n}")

main()
