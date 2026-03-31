table = []
# replace dots with x every tim command given
while True:
    size = int(input("Grid size: "))
    row = []
    for j in range(size):
        row.append(".")
    for k in range(size):
        table.append(row)

    direct = input("Direction: ")
    for row in table:
        print("".join(row))
    if direct == "":
        break
