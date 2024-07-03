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
    
class jefe(empleados):
    
    def __init__(self,nombre,apellido,edad,salario,dni,fech_vinc,empleaCarg):
        super.__init__(nombre,apellido,edad,salario,dni,fech_vinc)
        self.empleaCarg = empleaCarg
        
class area():
    
    def __init__(self,nombArea,desc,listEmp):
        self.__nombre= nombArea
        self.__Desc= desc
        self.__lista= listEmp
        
    def Agreg_emp(self):
        pass
        
    
emp1= empleados("Brian ","Florez",24,1350000,1061818886,"22-05-2024")
jef1= jefe("tomas ","Florez",24,1350000,1061818886,"22-05-2024")
##print(emp1.get_name_complet())

print("Jefe: ", jef1)
print("Empleado: ",emp1)
    
 
    
    