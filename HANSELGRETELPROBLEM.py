def init_table(size):
    tb=[];
    for k in range(size):
        row = []
        for j in range(size):
            row.append(".")

        tb.append(row)
    return tb


table = []
sizeNotSet = True
# replace dots with x every time command given
x = 0
y = 0
while True:
    if sizeNotSet == True:
        size = int(input("Grid size: "))
    sizeNotSet = False
    if not table:
        table = init_table(size)

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
