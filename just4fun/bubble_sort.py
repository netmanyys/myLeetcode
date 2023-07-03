# bubble sort
data = [89,57,121,23,56,34,25,17,13]
length = len(data)
for j in range(1,length):
    for i, n in enumerate(data[:-j]):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
    print(data)

# time complexity is O(n^2)
# space complexity is O(1)