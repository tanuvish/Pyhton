def factors (a):
    b=[]
    i=2
    while i < a:
        if a % i ==0:
            b.append(i)
            i += 1
            return b
        
        def common(a,b):
        comm = []
        for i in a :
            if i in b:
                comm.append(i)
                 return comm
             