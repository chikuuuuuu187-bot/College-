list1 = [5 , 4 , 3 ,2 ,1]

a = len(list1)
for i in range(0,a ):
    for j in range( 0 ,a - 1):
        if list1[j] > list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp 

for i in range(0 , a ):
    print(list1[i] , " ")