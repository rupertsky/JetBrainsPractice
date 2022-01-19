"""# write your code here
x = input()
chars = list(x)

def imposible(chars):

    count_x = chars.count('X')
    count_o = chars.count('O')

    if abs(count_x - count_o) >= 2:
        return True
    else:
        return False

def winner(chars):
    counter_x = 0
    counter_o = 0
    totalC = []

    if chars[0] is not None and chars[0] != "_" and chars[0] is chars[1] and chars[1] is chars[2]:
        if chars[0] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[0] is not None and chars[0] != "_" and chars[0] is chars[3] and chars[3] is chars[6]:
        if chars[0] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[0] is not None and chars[0] != "_" and chars[0] is chars[4] and chars[4] is chars[8]:
        if chars[0] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[1] is not None and chars[1] != "_" and chars[1] is chars[4] and chars[4] is chars[7]:
        if chars[1] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[2] is not None and chars[2] != "_" and chars[2] is chars[4] and chars[4] is chars[6]:
        if chars[2] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[2] is not None and chars[2] != "_" and chars[2] is chars[5] and chars[5] is chars[8]:
        if chars[2] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[3] is not None and chars[3] != "_" and chars[3] is chars[4] and chars[4] is chars[5]:
        if chars[3] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    if chars[6] is not None and chars[6] != "_" and chars[6] is chars[7] and chars[7] is chars[8]:
        if chars[6] == 'X':
            counter_x += 1
        else:
            counter_o += 1
    totalC.append(counter_x)
    totalC.append(counter_o)
    if counter_x == 0 and counter_o == 0:
        return None
    else:
        return totalC

def totalWins(o_x):
    xWins = 0
    oWins = 0
    if o_x is not None:
        if o_x[0] == 1:
            xWins += 1
        if o_x[1] == 1:
            oWins += 1
        if xWins == oWins:
            return True
        else:
            return False
    else:
        return False

print(f---------
#| {chars[0]} {chars[1]} {chars[2]} |
#| {chars[3]} {chars[4]} {chars[5]} |
#| {chars[6]} {chars[7]} {chars[8]} |
#---------)

if imposible(chars) or totalWins(winner(chars)):
    print("Impossible")
elif winner(chars) is not None:
    if winner(chars)[0] == 1:
        print("X wins")
    else:
        print("O wins")
elif winner(chars) is None and imposible(chars) is False and chars.count('_') == 0 and chars.count(None) == 0:
    print("Draw")
elif winner(chars) is None and imposible(chars) is False:
    print("Game not finished")
else:
    print("todo mal")
"""
X_O = input("Enter cells: ")
grid_slots = list(X_O)
grid_coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
confirm_coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]


def confirm_space(pos1, pos2, cor_list):
    for g in cor_list:
        if g[0] == pos1 and g[1] == pos2:
            return cor_list.index(g)


def new_grid(v_pos, coordinates, initial_slots):
    for i in initial_slots:
        for j in v_pos:
            if i == 'X' and i == initial_slots[j]:
                coordinates[j] = 'X'
            elif i == 'O' and i == initial_slots[j]:
                coordinates[j] = 'O'
    return coordinates


print(f"""---------
| {grid_slots[0]} {grid_slots[1]} {grid_slots[2]} |
| {grid_slots[3]} {grid_slots[4]} {grid_slots[5]} |
| {grid_slots[6]} {grid_slots[7]} {grid_slots[8]} |
---------""")

valid_pos = [val_pos for val_pos, val_char in enumerate(X_O) if val_char == 'X' or val_char == 'O']
grid_coordinates = new_grid(valid_pos, grid_coordinates, grid_slots)
empty_pos = []

for h, y in enumerate(grid_coordinates):
    if y != 'X':
        if y != 'O':
            empty_pos.append(h)

while True:
    try:
        x, y = map(int, input("Enter the coordinates: ").split())
        slot = confirm_space(x, y, confirm_coordinates)
        if 4 > x > 0 and 4 > y > 0:
            if grid_coordinates[slot] == 'X' or grid_coordinates[slot] == 'O':
                print("This cell is occupied! Choose another one!")
            else:
                for z in grid_coordinates:
                    if z[0] == x and z[1] == y:
                        pos = grid_coordinates.index(z)
                        grid_coordinates[pos] = 'X'
                break
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("You should enter numbers!")
for y in empty_pos:
    if grid_coordinates[y] != 'X':
        grid_coordinates[y] = '_'
    elif grid_coordinates[y] != 'O' and grid_coordinates[y] != 'X':
        grid_coordinates[y] = '_'

print(f"""---------
| {grid_coordinates[0]} {grid_coordinates[1]} {grid_coordinates[2]} |
| {grid_coordinates[3]} {grid_coordinates[4]} {grid_coordinates[5]} |
| {grid_coordinates[6]} {grid_coordinates[7]} {grid_coordinates[8]} |
---------""")
