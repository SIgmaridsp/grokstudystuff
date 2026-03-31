table = []
sizeNotSet = True
# replace dots with x every tim command given
while True:
    if sizeNotSet == True:
      size = int(input("Grid size: "))
    sizeNotSet = False
    row = []
    for j in range(size):
        row.append(".")
    for k in range(size):
        table.append(row)
    for row in table:
        print("".join(row))
    direct = input("Direction: ")
    if direct == "":
        break
