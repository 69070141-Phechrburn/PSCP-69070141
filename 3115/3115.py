"""Arcade of Time: Store Check"""
def main():
    """arcadehealjaii"""
    num,_ = map(int,input().split())
    open_stores = [0] * 1441
    for _ in range(num):
        start, stop = map(int, input().split())
        for minute in range(start, stop):
            open_stores[minute] += 1
    check_times = list(map(int, input().split()))
    results = []
    for k in check_times:
        results.append(open_stores[k])
    print(*results)

main()
