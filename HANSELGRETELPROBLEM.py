def init_table(size):
    tb=[];
    for k in range(size):
        row = []
        for j in range(size):
            row.append(".")
        tb.append(row)
        tb[x][y] = "x"
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

    for row in table:
        print("".join(row))
    direct = input("Direction: ")
    if direct == "":
        break
    else:
        if direct == "up":
            x -= 1
        elif direct == "down":
            x += 1
        elif direct == "left":
            y -= 1
        elif direct == "right":
            y += 1
        table[x][y] = "x"
