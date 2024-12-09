"""AOC 2024 - day 1 part 2"""

lines = open(r'day01/z1_input2.txt', 'r').read().split("\n")
rdc = {}
llst = []

for l in lines:
     els = l.split("   ")
     llst.append(els[0])
     if els[1] in rdc:
        rdc[els[1]] += 1 
     else:
        rdc[els[1]] = 1        

sm = 0

for el in llst:
    if el in rdc:
        sm = sm + ( int(el) * rdc[el])
         
print(sm)