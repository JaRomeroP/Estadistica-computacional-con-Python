#print("Hello world")

#name =input("Por favor dime tu nombre ")

#if len(name)!= 0:
   #print(f'one for {name} , one for me')
#else:
    #print('One for you, one for me')

n= int(input("Por favor ingresa tu numero "))

list = [3,5,7]

contador = 0
for numero in list:
   if n%numero==0:
      if numero ==3:
         print("pling")
         contador += 1
      if numero == 5:
         print("plang")
         contador +=1
      if numero == 7:
         print("plong")
         contador +=1
      if contador == 0:
         print(n) 
      
   
         
