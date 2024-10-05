
def int_roman(n):
    value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    num=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    
    add=""
    for i in range(len(value)):
        while n>=value[i]:
            add=add+num[i]
            n=n-value[i]
    
    print(add)  

n=int(input("Enter the number="))
int_roman(n)