arr = [1, 2, 3]
targe = 5
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print(f"Pair: {arr[i]+arr[j] == targe}, {arr[i]} + {arr[j]} = {arr[i]+arr[j]}")
