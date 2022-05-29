st = str(input())
cons = 0 
vow = 0
dig = 0 
wht_spa = 0 
for i in st:
    if i=='b' or  i=='c' or i =='d' or i=='f' or i=='g' or i=='h' or i=='j' or i=='k' or i=='l'or i=='m' or i=='n' or  i=='p' or i =='q' or i=='r' or i=='s' or i=='s' or i=='t' or i=='v' or i=='w'or i=='x' or i=='y' or  i=='z' or i =='B' or i=='C' or i=='D' or i=='F' or i=='G' or i=='H' or i=='J'or i=='K' or i=='L' or  i=='M' or i =='N' or i=='P' or i=='Q' or i=='S' or i=='T' or i=='V' or i=='W'or i=='X' or i=='Y' or  i=='Z':
        cons += 1 
    elif i=='a' or  i=='e' or i =='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O'or i=='U':
        vow += 1
    elif i== '0' or  i== '1' or i == '2' or i== '3' or i== '4' or i== '5' or i== '6' or i=='7' or i== '8' or i== '9' :  
        dig += 1
    else:
        wht_spa += 1
print(cons)
print(vow)
print(dig)
print(wht_spa)



