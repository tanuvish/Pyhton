stones = int (input("enter number of stones :"))
i=1
total=0
while True:
    total += 1
    if total >= stones :
        print("Ramesh won")
        break
    total += 2* i
    if total >=stones :
        print("suresh won")
        break
    i= i + 1
        