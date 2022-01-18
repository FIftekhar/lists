even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]

print("List of even numbers: " + str(even_numbers))
print("List of odd numbers: " + str(odd_numbers))

print("\nAdding the list of odd numbers to the end of the list of even numbers...")
print(str(even_numbers.extend(odd_numbers)))

print("\nThe same can be done in reverse: ")
print(odd_numbers.extend(even_numbers))

new_list = []
print("\nWe can also make our own lists.\n")
item_count = int(input("How many items do you want in your list? "))
print("")

for item in range(item_count):
    new_item = input("New item: ")
    new_list.append(new_item)

print("\nYour new list: " + str(new_list))