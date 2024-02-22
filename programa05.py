    Nombre:Leylani pg
    matricula:1723110391
    grupo:TI21
    Fecha:18/01/2024
    Descripcion:programa que crrea un objeto

"""


class Alumno:#define la clase
    matricula=None#atributo
    nombre=None#atributo
    def __init__(self,matricula,nombre):#constructor
        self.matricula=matricula#atributo
        self.nombre=nombre#atributo
        print("objeto Alumno")#imprime el objeto
    def estudiar(self):#metodo
        print(f"{self.nombre} esta estudiando")#imprime el metodo
    def sumar(self, numero1, numero2):#metodo
        suma=numero1+numero2#atributo
        print(f"la suma es: {suma}")#imprime el metodo

dejah=Alumno("1111","Dejah")#crea un objeto
dejah.estudiar()#llama el metodo
dejah.sumar(10,5)#llama el metodo

