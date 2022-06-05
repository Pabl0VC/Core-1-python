#1. Básicos
for i in range(151):
    print(i)


#2. Multiplos de 5
for m in range(5,1001,5):
    print(m)


#3. Contar, a la manera Dojo
for cd in range(1,101):
    if cd % 5 == 0 and not cd % 10==0:
        print("Coding")
    if cd % 10 == 0: 
        print("Coding Dojo")
    else:
        print(cd)
    

#4. Whoa. Es un gran idiota
suma = 0
for impar in range (500001):
    if not impar % 2 ==0:
        suma = suma + impar
print(suma)

#5. Cuenta regresiva de a 4
for regre in range(2018,0,-4):
    print(regre)


#6. Contador flexible
lowNum = 2
highNum = 9
mult = 3
for jj in range(lowNum,highNum+1):
    if jj % mult ==0:
        print (jj)



