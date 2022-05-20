import array 

lista  = array.array('i', [1,2,3,4,5,6])

print("El nuevo elemento creado es : ", end = "")
for i in range (0, 5):
    print (lista[i], end =" ")

print ("\r")

print ("El elemento eliminado es : ", end ="")
print (lista.pop(2))

print ("La lista despues de la eliminada es : ", end ="")
for i in range (0, 4):
        print (lista[i], end =" ")
"""
\r\ significa 
\r\ significa 
"""
print ("\r")


