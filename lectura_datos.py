#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Se pide el nombre al usuario
print ("Hola, ¿cómo te llamas?")
#Se leen los datos introducidos por el usuario y se asignan a la variable nombre
nombre = input()
#Se escribe el nombre solicitado
print ("Buen día {}".format(nombre))


# In[ ]:


print ("---Calculadora---") #Opciones para el usuario
print ("1- Sumar")
print ("2- Restar")
print ("3- Multiplicar")
print ("4- Dividir")
print ("5- Salir")


# In[ ]:


op = int(input('Opcion: '))

