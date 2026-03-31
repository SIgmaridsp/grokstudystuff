table = []
sizeNotSet = True
# replace dots with x every tim command given
y = 0
x = 0
while True:
    if sizeNotSet == True:
        size = int(input("Grid size: "))
    sizeNotSet = False
    for k in range(size):
        row = []
        for j in range(size):
            row.append(".")
        table.append(row)
    table[x][y] = "x"
    for row in table:
        print("".join(row))
    direct = input("Direction: ")
    if direct == "":
        break
    else:
        if direct == "up":
            y -= 1
        elif direct == "down":
            y += 1
        elif direct == "left":
            x -= 1
        elif direct == "right":
            x += 1
        table[y][x] = "x"
