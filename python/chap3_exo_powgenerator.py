import random as rd
x = int(rd.random()*1000)/100.
n = int(rd.random()*3+1)
if rd.random() < 0.5:
    n *= -1
print("$" + str(int(x)) + "{,}" + str(int((x-int(x))*100)) + "\\times 10^{" + str(int(n)) + "}$" )