nombre = input("ingrese su nombre: ")
print("Bienvenido", nombre)
valor1 = int(input("ingrese valor de su primer producto: "))
valor2 = int(input("ingrese valor de su segundo producto: "))
valor3 = int(input("ingrese valor de su tercer producto: "))
total = valor1 + valor2 + valor3
print(total)
pago = int(input("ingrese con cuanto va a pagar: "))
devuelta = pago - total 
print(f"Su devuelta es:", devuelta)

