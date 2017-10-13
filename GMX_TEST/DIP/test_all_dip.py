from pmx import *

res_ids =[
'A',
'G',
'I',
'L',
'P',
'V',
'F',
'W',
'Y',
'D',
'E',
'R',
'H',
'K',
'S',
'T',
'C',
'M',
'N',
'Q',
]
print(len(res_ids))
num = 0
for i in res_ids: 
    num = num +1
    print(num)
    sequence = "%s%s%s"%(i,i,i)
    c = Chain().create( sequence )
    c.write("DIP_%s.pdb"%i)
