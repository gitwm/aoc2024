"""AOC 2024 - day 1 part 1"""

with open(r'day01/z1_input1.txt', 'r') as file:
     txt = file.read()

lines = txt.split("\n")
rlst = []
llst = []

for l in lines:
     els = l.split("   ")
     rlst.append(els[0])
     llst.append(els[1])

rlst.sort()
llst.sort()

sm = 0

for i in range(len(rlst)):
     if int(rlst[i]) < int(llst[i]):
         sm = sm + int(llst[i]) - int(rlst[i])
     else:
         sm = sm + int(rlst[i]) - int(llst[i])
         
print(sm)