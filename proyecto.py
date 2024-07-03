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
    
class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []
        self.jefe_area = None
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado) and empleado not in self.empleados:
            self.empleados.append(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} agregado al área {self.nombre}.")
    
    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} eliminado del área {self.nombre}.")
    
    def asignar_jefe(self, jefe):
        if isinstance(jefe, Jefe):
            self.jefe_area = jefe
            print(f"Jefe {jefe.obtener_nombre_completo()} asignado al área {self.nombre}.")
    
    def obtener_jefe_area(self):
        return self.jefe_area.obtener_nombre_completo() if self.jefe_area else "Ninguno"
    
    def obtener_empleados(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados]
    
    def obtener_informacion(self):
        empleados_str = ", ".join(self.obtener_empleados()) or "Ninguno"
        jefe_str = self.obtener_jefe_area()
        return f"Área: {self.nombre}, Descripción: {self.descripcion}, Jefe: {jefe_str}, Empleados: {empleados_str}"

    
    