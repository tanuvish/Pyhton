a=[2 , 5, 8, 11, 14, 17, 20]
sum =0
aplength = len(a)
for i in range (0,aplength):
    if a [i]==a[aplength]:
        print("nth term is :",a[i])
        
        for i in range (0, aplength):
            sum=sum +a[i]
            
            print("sum of arithemetic series is :", sum)