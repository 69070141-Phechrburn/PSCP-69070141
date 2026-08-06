"""CU"""
def main():
    """cu"""
    aeiou = input().lower()
    a = 0
    e = 0
    eye = 0
    o = 0
    u = 0
    for i in aeiou:
        if i == "a":
            a += 1
        elif i == "e":
            e += 1
        elif i == "i":
            eye += 1
        elif i == "o":
            o += 1
        elif i == "u":
            u += 1
    if a > 0:
        print(f"a : {a}")
    if e > 0:
        print(f"e : {e}")
    if eye > 0:
        print(f"i : {eye}")
    if o > 0:
        print(f"o : {o}")
    if u > 0:
        print(f"u : {u}")

main()
