n = int(input())
book = dict()
for _ in range(n):
    title = input()
    if title not in book:
        book[title] = 1
    else:
        book[title] += 1

best = [0,'']
for key, val in book.items():
    if val>best[0]:
        best[0] = val
        best[1] = key
    elif val==best[0]:
        if key<best[1]:
            best[1] = key

print(best[1])