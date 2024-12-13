"""AOC 2024 - day 2 part 2"""

lines = open(r'day02/input2b.txt', 'r').read().split("\n")
#lines = open(r'day02/test.txt', 'r').read().split("\n")

sm = 0 

def rules(rep, rm = -1):
    lst = [int(x) for x in rep.split()]
    if rm > -1:
        del lst[rm]

    if lst[0]<lst[1]:
        inc = True
    else: 
        inc = False

    for i in range(1, len(lst)):
        diff = lst[i-1] - lst[i]
        # rule 1
        if inc: 
            if diff > 0: return False
        else:
            if diff < 0: return False
        # rule 2
        if diff < -3 or diff > 3 or diff == 0: return False  
    return True

for rep in lines:
   if rules(rep):
       sm += 1
   else:       
       dl = len(rep.split())
       ok2 = False
       for i in range(dl):
           if rules(rep, i):
               ok2 = True
               break   
       if ok2:
           sm += 1
             
print("sm =",sm)
#665