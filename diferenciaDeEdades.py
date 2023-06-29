maria =int(input("La edad de maria es "))
edad_pedro =int(maria*2+4) 
edad_jose  = int((3*maria+4)//5)
pedro =("La edad de pedro es = " + str(maria*2 + 4))
jose  =("La edad de jose es = " + str((3*maria + 4)//5))
print(pedro,jose)
if edad_jose <= 20:
  print("uno")
else:
  if edad_jose <= 30:
   print("dos")
  else:
   if edad_jose >= 31:
    print("tres")

'''
proyecto que calcula la diferencia de edades.
Edad de pedro (es el doble de la edad de maria + 4).
La edad de jose (es 3 veces la de maria +4 /5)
'''