lst = input().split()
lst1 = input().split()
count=0
for i in lst:
    for j in lst1:
        if i==j:
            count+=1
if count == len(lst1):
    print('True')
else:
    print("false")