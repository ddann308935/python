# prompt user for 7 integers and display even ones

num_list = []
i = 0

while i < 7:
    num = int(input("Enter an integer: "))
    num_list.append(num)
    i += 1

num_list = num_list.sort()
print("Even numbers from this set are: ", end="")

n = 0
while n < 7:
    if (list[n] % 2) == 0:
        print(f"{num_list[n]}, ", end=" ")
print()

