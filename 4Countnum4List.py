l = [1,2,3,4,5,6,4,7,3,4]
count = 0
for i in range(len(l)):
    if(l[i] == 4):
        count = count + 1
print(count ,"times 4 is occuring")