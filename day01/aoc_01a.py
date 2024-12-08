"""AOC 2024 - day 1a"""

with open(r'C:\Users\wmokrzan\Downloads\z1_input1.txt', 'r') as file:
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
     if int(rlst[i])<int(llst[i]):
         sm = sm + int(rlst[i])-int(llst[i])
     else:
         sm = sm + int(llst[i]) - int(rlst[i])

print(sm)

#print(rlst)
