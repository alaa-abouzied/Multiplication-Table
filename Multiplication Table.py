num = input("Enter number: ")
arr = []
for i in range(int(num)):
    item = []
    for j in range(i+1):
        item.append((j+1)*(i+1))
    arr.append(item)
print(arr)
