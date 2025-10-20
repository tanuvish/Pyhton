minskill=100
skills = []
peoples=int(input("enter number of people :"))
for i in range(peoples):
    push=int(input(f"enter person {i+1} skill :"))
    skills.append(push)
    
    for i in range (peoples) :
        if skills[i] >= minskill :
            print("yes")
        else:
            print("no")
           