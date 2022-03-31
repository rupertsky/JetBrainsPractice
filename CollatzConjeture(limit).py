terms = 0
counter = 0
while True:
    n, y = map(int, input().split())
    x = n
    counter += 1
    while n > 0 and y > 0:
        if x <= y:
            terms += 1
            if x == 1:
                print(f"Case {counter}: A = {n}, limit = {y}, number of terms = {terms}")
                break
            elif x % 2 == 0:
                x //= 2
            else:
                x = (x * 3) + 1
        else:
            print(f"Case {counter}: A = {n}, limit = {y}, number of terms = {terms}")
            break
    if n < 0 or y < 0:
        break
    else:
        terms = 0
