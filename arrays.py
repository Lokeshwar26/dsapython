
num = int(input("How many elements to be in the array? "))


arr = []


print(f"\nEnter your {num} elements:")
for i in range(num):
    element = input(f"Element {i + 1}: ")
    arr.append(element)

print("\nThe elements of the array are:")
for i in range(num):
    print(arr[i], end=" ")
