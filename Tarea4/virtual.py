class inicializacion:
    def __init__(self, size):
        self.size = size
        self.T = [None] * size
        self.a = [None] * size
        self.b = [None] * size
        self.counter = 0

    def asignar_valor(self, pos, val):
        if pos < 0 or pos >= self.size:
            print("Error: Posición no válida.")
            return
        if not self.consultar_status(pos): 
            self.a[self.counter] = pos
            self.b[pos] = self.counter
            self.T[pos] = val
            self.counter += 1
            return
        
        self.T[pos] = val
        return

    def consultar_status(self, pos):
        if self.b[pos] != None and 0 <= self.b[pos] <= self.counter:
            if self.a[self.b[pos]] == pos:
                return True
            else:
                return False
        else:
            return False
        
    def imprimir_status(self, pos):
        if self.consultar_status(pos):
            print(f"Posición {pos} inicializada con valor {self.T[pos]}.")
        else:
            print("Posición no inicializada.")
        return

    def limpiar(self):
        self.T = [None] * self.size
        self.a = [None] * self.size
        self.b = [None] * self.size
        self.counter = 0

def main():
    size = int(input("Ingrese el tamaño del arreglo: "))
    client = inicializacion(size)

    while True:
        choice = input("Seleccione una opción (ASIGNAR, CONSULTAR, LIMPIAR): ").split()

        if choice[0] == 'asignar' or choice[0] == 'ASIGNAR':
            if len(choice) < 3:
                print("Error: faltó información.")
                continue
            pos = int(choice[1])
            val = int(choice[2])
            client.asignar_valor(pos, val)

        elif choice[0] == 'consultar' or choice[0] == 'CONSULTAR':
            if len(choice) < 2:
                print("Error: faltó información.")
                continue
            pos = int(choice[1])
            client.imprimir_status(pos)

        elif choice[0] == 'limpiar' or choice[0] == 'LIMPIAR':
            client.limpiar()

        elif choice == 'SALIR':
            break

        else:
            print(choice[0])
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
