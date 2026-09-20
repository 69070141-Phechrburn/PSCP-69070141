"""spacerrker"""
def main():
    """spacerbigger"""
    words = [input() for _ in range(5)]
    long = max(len(w) for w in words)
    print("*" * (long + 4))
    for i in words:
        print(f"* {i:<{long}} *")
    print("*" * (long + 4))

main()
