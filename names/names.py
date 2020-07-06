import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# O(n^2) - 64 duplicates - 5.7245824337005615 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# O(n^2 or O(n log n)?: hard to say what python is really doing here - 64 duplicates - 1.290999174118042 seconds
# for name in names_2:
#     if name in names_1:
#         duplicates.append(name)

## 1: create BST from names_1
bst = BSTNode(names_1[0])
for name in names_1[1:]:
    bst.insert(name)

## 2: search tree for names_2 values
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
