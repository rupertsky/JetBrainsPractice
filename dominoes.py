import random


def pieces():
    total_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
    [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
    [3, 3], [3, 4], [3, 5], [3, 6],
    [4, 4], [4, 5], [4, 6],
    [5, 5], [5, 6],
    [6, 6]]
    return total_pieces


def distribution():
    x = pieces()
    random.shuffle(x)
    stock = x[:14]
    computer = x[14:21]
    player = x[21:]
    return stock, computer, player


def comp_player(c, p):
    sum_c = 0
    top_c = []
    sum_p = 0
    top_p = []
    for i in c:
        counter = sum(i)
        if counter > sum_c:
            sum_c = counter
            top_c = i
        elif counter == sum_c:
            if i[0] == i[1]:
                top_c = i
    for j in p:
        counter = sum(j)
        if counter > sum_p:
            sum_p = counter
            top_p = j
        elif counter == sum_p:
            if j[0] == j[1]:
                top_p = j
    return top_c, top_p


def snake_status(c, p):

    csum = sum(c)
    psum = sum(p)

    if csum > psum:
        return c
    else:
        return p


def log(s, c, p, ds, stat):
    print(f"""Stock pieces: {s}
Computer pieces: {c}
Player pieces: {p}
Domino snake: {ds}
Status: {stat}""")


def main():
    while True:
        s, c, p = distribution()
        comp, player = comp_player(c, p)
        if comp[0] != comp[1] and player[0] != player[1]:
            continue
        else:
            snake = [snake_status(comp, player)]
            if snake[0] in c:
                c.remove(snake[0])
                log(s, c, p, snake, 'player')
                break
            else:
                p.remove(snake[0])
                log(s, c, p, snake, 'computer')
                break


main()
