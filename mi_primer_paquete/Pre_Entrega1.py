
  
def  validador (username, password):
 #USERNAME
    largo_u = False 
    mayus_u =False
    numer_u =False 

    if len (username)>1 and len(username) <=20 :
        largo_u =True
    else:
        largo_u = False
        
    for i in range (len(username)) :
        if username [i].isupper():
             mayus_u =True
        if username [i].isnumeric():
             numer_u=True


#PASSWORD

    largo_p = False 
    mayus_p =False
    numer_p =False

    if len (password)>1 and len (password) <=20 :
         largo_p =True

    
        
    for i in range (len(password)):
        if password [i].isupper():
                mayus_p =True
        if password [i].isnumeric():
                numer_p=True




    if largo_u and mayus_u and numer_u and largo_p and mayus_p and numer_p:  
         print ("Bien,lo lograste  :)" )
         return True 
    else :
          print ("Intentalo otra vez...  ")
          return False 


while True:
    username  = input ("Ingresa usuario aqui:  ")
    password  = input ("Ingresa clave aqui:    ")

    resultado = validador (username, password)

    if resultado == True:
         break



# Diccionario para almacenar usuarios y contraseñas
almacenamiento = {}
#funcion de registro
def registro_usueario_password (almacenamiento, username, password):
    
    if  validador(username,password):
        validador_res = True
    else:
        print(" No es válido. Debe contener mayúsculas, minúsculas y números.")


    almacenamiento[username] = password
    print("Usuario registrado exitosamente.")
            
    
resultado = registro_usueario_password (almacenamiento, username, password)

print(almacenamiento)


#Verificar si el username y password si coinciden 


def verificar_usuario_password (almacenamiento, username, password): 
    if username in almacenamiento:

        if almacenamiento[username]== password: 
            print ("Bien, ya tienes acceso" )
            return True
        else: 
             print ("Lo siento el password no coincide" )
             return False
    else : 
            print ("Username no encontrado .. :( ")
            return False
     
     
resultado = verificar_usuario_password (almacenamiento, username, password)  
print (almacenamiento)
almacenamiento = {}


    

#User : ASD123434
#Password : QWEER1234