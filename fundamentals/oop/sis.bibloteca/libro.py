class Libro:
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.list = []

    def prestar_un_libro(self):
        titulo = input("Ingresa nombre del libro: ")
        for i in self.list:
            if i.titulo == titulo:
                print("Prestar el libroi")
            else:
                print("Lo sentimos este libro no esta disponible :()")   
    
    
    def devolver_libro(self):
        titulo = input("Ingresa el nombre del libro: ")
        titulo = titulo
        print("Gracias por devolver el libro :)")
                
            
    
    def eliminar_libro(self, titulo):
        for x in self.list:
            if x.titulo == titulo:
                x.remove
    
    
    def agregar_libro(self):
        print("Agregar libro.... ")
        titulo = input("Ingresar nombre del libro:")
        autor = input("Ingresar el autor del libro:")
        fecha = input("Ingresar año de publicación:")

        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha