#Khayal Khuduzada 6523a5 N025
s=0
x=3
n=1
z=1
while x/n > 0.001:
    n*=z
    s+=x/n
    x+=1
    z+=1
print(s)
