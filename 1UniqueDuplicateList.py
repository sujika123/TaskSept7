# input a list from user and extract unique and duplicate values into a new list

# creating an empty list
lst = []
ul = []
dl = []

# number of elements as input
n = int(input("Enter number of elements : "))

print("Enter the elements ")
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)

print("List is ",lst)

for x in lst:
    if x not in ul:
        ul.append(x)
    elif x not in dl:
        dl.append(x)

print("Unique list : ",ul)
print("Duplicate list : ",dl)






