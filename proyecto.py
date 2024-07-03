from datetime import datetime

class Empleado:
    def __init__(self, nombre, apellido, edad, salario, id, fech_vinc):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.id = id
        self.fech_vinc = datetime.strptime(fech_vinc, '%Y-%m-%d')
    
    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def obtener_sueldo(self):
        return self.salario
    
    def obtener_informacion(self):
        return (f"Nombre: {self.obtener_nombre_completo()}, Edad: {self.edad}, Salario: {self.salario}, "
                f"DNI: {self.id}, Fecha de vinculación: {self.fech_vinc.strftime('%Y-%m-%d')}")

class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, id, fech_vinc):
        super().__init__(nombre, apellido, edad, salario, id, fech_vinc)
        self.empleados_a_cargo = []
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado) and empleado not in self.empleados_a_cargo:
            self.empleados_a_cargo.append(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} agregado bajo el cargo del jefe {self.obtener_nombre_completo()}.")
    
    def eliminar_empleado(self, empleado):
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} eliminado bajo el cargo del jefe {self.obtener_nombre_completo()} (notificación de despido).")
    
    def obtener_empleados_a_cargo(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados_a_cargo]
    
    def obtener_informacion(self):
        empleados_str = ", ".join(self.obtener_empleados_a_cargo()) or "Ninguno"
        return super().obtener_informacion() + f", Empleados a cargo: {empleados_str}"
    
 
    
    