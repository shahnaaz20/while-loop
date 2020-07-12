num = int(input("from which table u want"))
num2 = int(input("Till which table u want"))
while num <= num2:
    i=1
    while i <= 10:
        product = num*i
        print(num,'*',i,'=',product)
        i=i+1
    print(' ')
    num=num+1
