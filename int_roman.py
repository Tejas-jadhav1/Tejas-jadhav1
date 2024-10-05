
value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
num=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

n=int(input("Enter the number="))
add=""
for i in range(len(value)):
    while n>=value[i]:
        add=add+num[i]
        n=n-value[i]
    
print(add)