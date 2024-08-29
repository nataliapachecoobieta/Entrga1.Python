class Cliente :

    def __init__(self,id,name,lastName,age, mail,payment_method ):
        self.id= id 
        self.name = name
        self.lastName =lastName
        self.age =age
        self.mail = mail
        self.payment = payment_method

    def informacion_cliente (self):
        
        return f"Cliente:  {self.name} {self.lastName}, RUN : {self.id}, Edad {self.age} , Mail {self.mail}, Metodo de Pasgo {self.payment}"
    
    def __str__(self):
        return self.informacion_cliente()
    

    def mayor_edad(self):
        return self.age >= 18


    def cambiar_metodo_pago(self, nuevo_metodo_pago): 
        self.payment = nuevo_metodo_pago
        return f"Método de pago actualizado a {self.payment}"
