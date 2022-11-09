first_integer = int(input(""))
second_integer = int(input(""))

if first_integer <= second_integer:
    for temp in range(first_integer, second_integer + 1, 5):
        print(temp, end=" ")
    print()

else:
    print("Second integer can't be less than the first.")
