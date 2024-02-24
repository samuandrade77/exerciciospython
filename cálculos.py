try:
    primeiro_numero = float(input ("digite o primeiro número:"))
    segundo_numero = float(input ("digite o segundo número:"))
    resultado = primeiro_numero/segundo_numero
    print(f"resultado: {resultado: .1f} ") 
except ZeroDivisionError:
    print("resultado inexistente")
    