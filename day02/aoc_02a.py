"""AOC 2024 - day 2 part 1"""

lines = open(r'day02/input2a.txt', 'r').read().split("\n")
#lines = open(r'day02/test.txt', 'r').read().split("\n")

sm = 0 

def rules (rep):
    lst = [int(x) for x in rep.split()]
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
        if diff < -3 or diff > 3 or diff == 0:
            return False  
    return True

for rep in lines:
   if rules(rep):
       sm += 1 
   
print("sm =",sm)