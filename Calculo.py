class calculadora:
    def __init__(self):
        self.vector=[]
        self.suma=0
        self.a=0
        self.b=0

        
    def Sumaa(self,a,b):
        self.a=int(a)
        self.b=int(b)      
        self.suma = self.a+self.b
        self.vector.append(a+"+"+b+"="+str(self.suma))
        random=str(self.suma)
        return "{\"data\":\""+random+"\"}"
    

    def Resta(self,a,b):
        self.a=int(a)
        self.b=int(b)
        self.suma = self.a-self.b
        self.vector.append(a+"-"+b+"="+str(self.suma))
        random=str(self.suma)
        return "{\"data\":\""+random+"\"}" 



    def Multii(self,a,b):
        self.a=int(a)
        self.b=int(b)
        self.suma = self.a*self.b
        self.vector.append(a+"*"+b+"="+str(self.suma))
        random=str(self.suma)
        return "{\"data\":\""+random+"\"}"

    def Divii(self,a,b):
        self.a=int(a)
        self.b=int(b)
        self.suma = self.a/self.b
        self.vector.append(a+"/"+b+"="+str(self.suma))
        random=str(self.suma)
        return "{\"data\":\""+random+"\"}"

    def Pote(self,a,b):
        self.a=int(a)
        self.b=int(b)
        self.suma = self.a**self.b
        self.vector.append(b+"^"+a+"="+str(self.suma))
        random=str(self.suma)
        return "{\"data\":\""+random+"\"}" 

    def raizz(self,a,b):
        self.a=int(a)
        self.b=int(b)
        self.suma = self.a**(1/self.b)
        self.vector.append(a+"sqrt"+b+"="+str(self.suma))
        random=str(self.suma)
        return "{\"data\":\""+random+"\"}"
    
    def obtenerUser(self):
        texto="["
        for i in range(0,len(self.vector)):
            texto="{"
            texto+=f"\"data\":\"{self.vector[i]}\""
            texto+="},"
        return texto+"{\"data\":\"\"}]"
            

   

        


   
    



# texto+=f"\"Operación\":\"{self.vector[i]}\""