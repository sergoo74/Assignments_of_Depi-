# 1
# Define the lists
list1 = [3, 1, 4]
list2 = [2, 5, 0]

# Step 1: Merge the lists
list = list1 + list2
# Step 2: Sort the merged list using Bubble Sort
for i in range(len(list)):
    for j in range(0, len(list) - i - 1):
        if list[j] > list[j + 1]:
            # Swap if the element found is greater than the next element
            list[j], list[j + 1] = list[j + 1],list[j]

# Print the sorted  list
print(list)

#2
s = "abc"
n = 3
result = "".join([char * n for char in s])# Repeat each character 'n' times and use join to concatenate the result
print(result)# "aaabbbccc"

#(slides)
#1
print(5+3)  #Addition
print(10-2)  #Subtraction
print(4*2)  #Multiplication
print(16/2)   #Division

# 2
sentence = "this is a string"
# Replace spaces with hyphens
modified_sentence = sentence.replace(" ", "-")
print(modified_sentence)

# 3
n_Friends = ["Mohamed", "ALi", "Mahmoud"]
for name_f in n_Friends:
    print(f"Hi {name_f}, I'd like to invite you to dinner.")
# 4
# a)
print(f"Unfortunately, {n_Friends[1]} can't make it to dinner.")
# b)
n_Friends[1] = "Galal"
# c)
for guest in n_Friends:
    print(f"Dear {name_f}, you are still invited to dinner.")
# 5
# a)
print("I found a bigger dinner table! I can invite more guests.")
# b)
n_Friends.insert(0, "Mossad")
# c)
n_Friends.insert( 2, "ibrahim")
# d)
n_Friends.append("mona")
# e)
for name_f in n_Friends:
    print(f"Dear {name_f}, you are invited to dinner.")


