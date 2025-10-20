work = int (input (" enter number of works :"))
for i in range (work):
    SH = int(input(f"enter starting hour of work { i+1} : "))
    SM = int(input(f"enter starting minute of work { i+1} : "))
    EH = int(input(f"enter ending hour of work { i+1} : "))
    EM = int(input(f"enter ending  minute of work { i+1} : "))
    
    start = SH * 60 + SM
    end = EH * 60 * EM
    duration = end - start
    hour= duration // 60 
    minute = duration % 60
    
    print(f"you worked {hour} hr { minute} min ")