words = ["Alpha", "Bravo", "Romeo", "Echo", "Charlie", "Foxtrot", "Delta", "Golf", "Tango", "Whiskey", "Foxtrot"]
numbers = [1, 5, 10, 7, 14, 22, 13, 2, 1, 1, 4, 8]

# We can search for items in lists.

print("Index of 'Romeo': " + str(words.index("Romeo")))
print("Index of '22': " + str(numbers.index(22)))

# We can count how many items are in a list.

print("The word 'Foxtrot' appears " + str(words.count("Foxtrot")) + " times in the 'words' list.")
print("The number '1' appears " + str(numbers.count(1)) + " times in the 'numbers' list.")

# We can sort lists as well.

print("The 'words' list sorted: " + str(words.sort()))
print("The 'numbers' list sorted: " + str(numbers.sort()))

# Lists can be reversed.

print(str(words.reverse()))
print(str(numbers.reverse()))