class empleados():
  
    def __init__(self,nombre,apellido,edad,salario,dni,fech_vinc):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = salario
        self.__dni=dni
        self.__fech_vinc= fech_vinc
        
    def get_name_complet(self):
        name=self.__nombre + self.__apellido
        return name
    
    
    
    
emp1= empleados("Brian ","Florez",24,1350000,1061818886,"22-05-2024")

print(emp1.get_name_complet())
    
 
    
    