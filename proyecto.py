from datetime import datetime

class Empleado:
    def __init__(self, nombre, apellido, edad, salario, id, fech_vinc):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__salario = salario
        self.__id = id
        self.__fech_vinc = datetime.strptime(fech_vinc, '%Y-%m-%d')
    
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    def get_sueldo(self):
        return self.salario
    
    def get_informacion(self):
        return (f"Nombre: {self.nombre_completo()}, Edad: {self.__edad}, Salario: {self.__salario}, "
                f"Cédula: {self.__id}, Fecha de vinculación: {self.__fech_vinc.strftime('%Y-%m-%d')}\n")

class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, id, fech_vinc):
        super().__init__(nombre, apellido, edad, salario, id, fech_vinc)
        self.empleados_a_cargo = []
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado) and empleado not in self.empleados_a_cargo:
            self.empleados_a_cargo.append(empleado)
            print(f"Empleado {empleado.nombre_completo()} agregado bajo el cargo del jefe {self.nombre_completo()}.\n")
    
    def eliminar_empleado(self, empleado):
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)
            print(f"Empleado {self.nombre_completo()} eliminado bajo el cargo del jefe {self.nombre_completo()} (notificación de despido).\n")
    
    def get_empleados_a_cargo(self):
        return [empleado.nombre_completo() for empleado in self.empleados_a_cargo]
    
    def get_informacion(self):
        empleados_str = ", ".join(self.get_empleados_a_cargo()) or "Ninguno"
        return super().get_informacion() + f"\nEmpleados a cargo: {empleados_str}\n"
    
class Area:
    def __init__(self, nombre, descripcion):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.empleados = []
        self.jefe_area = None
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado) and empleado not in self.empleados:
            self.empleados.append(empleado)
            print(f"Empleado {empleado.nombre_completo()} agregado al área {self.__nombre}.\n")
    
    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            print(f"Empleado {empleado.nombre_completo()} eliminado del área {self.nombre}.\n")
    
    def asignar_jefe(self, jefe):
        if isinstance(jefe, Jefe):
            self.jefe_area = jefe
            print(f"Jefe {jefe.nombre_completo()} asignado al área {self.__nombre}.\n")
    
    def get_jefe_area(self):
        return self.jefe_area.nombre_completo() if self.jefe_area else "Ninguno"
    
    def obtener_empleados(self):
        return [empleado.nombre_completo() for empleado in self.empleados]
    
    def get_informacion(self):
        empleados_str = ", ".join(self.obtener_empleados()) or "Ninguno"
        jefe_str = self.get_jefe_area()
        return f"Área: {self.__nombre}, Descripción: {self.__descripcion}\nJefe Área: {jefe_str}, Empleados: {empleados_str}"

    
empleado1 = Empleado("Juan", "Pérez", 30, 50000, "12345678", "2020-01-15")
empleado2 = Empleado("Ana", "García", 28, 48000, "87654321", "2021-03-10")

jefe = Jefe("Carlos", "López", 45, 70000, "11223344", "2015-06-01")
jefe.agregar_empleado(empleado1)
jefe.agregar_empleado(empleado2)

area = Area("Desarrollo", "Área encargada del desarrollo de software")
area.agregar_empleado(jefe)
area.agregar_empleado(empleado1)
area.agregar_empleado(empleado2)
area.asignar_jefe(jefe)

print(empleado1.get_informacion())
print(empleado2.get_informacion())
print(jefe.get_informacion())
print(area.get_informacion())  