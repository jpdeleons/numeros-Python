listaNumeros =  []
numeroUsuario = int(input("Buena onda vaya ingresando sus numeritos: "))
listaNumeros.append(numeroUsuario)

decision = input("Queres mas Numeros? Puchale a la S: ")

while decision == "s" or decision == "S":
    numeroUsuario  = int(input("Vaya metale mas numeritos pues: "))
    listaNumeros.append(numeroUsuario)
    decision = input("Queres mas numeros mi chavo o le paramos? ")

max_numerito = max(listaNumeros)
print(f"los numeritos son  {max_numerito}")
input("Puchele otra tecla para pararla ")