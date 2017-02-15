# Chapter 3 - Strings, Lists, Tuples, and Maps

# In this chapter, you learned how Python uses strings to
# store text, and how it uses lists and tuples to handle
# multiple items. You saw that the items in lists can be
# changed, and that you can join one list to another list,
# but that the values in a tuple cannot change. You also
# learned how to use maps to store values with keys that
# identify them.

# Note the above chapter name and intro are from the book,
# and the examples listed below are a combination from the
# book and some created by myself, Mark Blais.


# What I Learned...

# These are strings.
print('This is a single quote string.')
print("This is a double quote string.")
print('''This is a triple quote string.''')

# This is escaping using \.
print('He said, "Aren\'t can\'t shouldn\'t wouldn\'t."')
print("He said, \"Aren't can't shouldn't wouldn't.\"")
print('''He said, "Aren't can't shouldn't wouldn't."''')

# Embedding a value into a string using %s.
myscore = 1000
message = 'I scored %s points.'
print(message % myscore)

# Multiplying strings.
print(10 * 'a')

# This is a list stored in a variable.
list = ['item-1', 'item-2', 'item-3']
print(list)

# Printing item(s) from the list.
print(list[0])
print(list[1])
print(list[2])
print(list[0:2])
print(list[1:3])

# A list containing text, integers and floats.
list = ['item-1', 'item-2', 'item-3', 'or', 5, 10, 15, 'or', 5.0, 10.0, 15.0]
print(list)

# Replacing item(s) in the list.
list[1] = 'replacement'
list[5] = 'replacement'
list[9] = 'replacement'
print(list)

# Removing item(s) from the list.
del list[1]
del list[4]
del list[7]
print(list)

# Adding item(s) to the end of the list.
list.append('addition')
list.append('another addition')
print(list)

# Adding together a list of numbers and a list of strings.
string_list = ['string', 'string', 'string']
number_list = [1, 2, 3]
print(string_list + number_list)

# Multiply a list.
print(number_list * 3)
