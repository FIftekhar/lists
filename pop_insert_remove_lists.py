words = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
print("This is what our initial list looks like: \n" + str(words) + "\n")

# The 'pop' function takes the last item in the list off the list.

words.pop() # removes 'Foxtrot'
print("This is what the list looks like after we use 'pop': \n" + str(words))

print("\nWe can also use the 'insert' function to place an item in the list.\n")

# 'Insert' takes 2 parameters: the index and the item

index = int(input("Which index would you like to insert your item? "))
new_word = input("What word do you want to input? ")
words.insert(index, new_word) # inserts new_word at the index
print("\nThis is what the list looks like after we use 'insert': \n" + str(words))

# The 'remove' function takes an index as a parameter and removes the item at that index from the list.

print("\nWe can also remove items from the list.")
remove_this = input("Indicate the word you would like to remove: ")

words.remove(remove_this)
print("This is what the list looks like after we use the 'remove' function: " + str(words))

print("\nThis is what happens if we use the 'clear' function: ")
print(str(words.clear()))
print("It says 'None' because there is no list to show anymore!")