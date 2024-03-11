def big_mac():
   print("sanduiche big mac")

#print("inicio")
#big_mac()    
#print("fim")

def fazer_big_mac(nome):
    print("sanduiche big mac", nome)

#fazer_big_mac("samuel")

def fazer_batata(tamanho):
    print("batata", tamanho)     
    
def preparar_refrigerante(tipo, tamanho):
   print(tipo, tamanho)    

#fazer_big_mac("samuel")   
#fazer_batata("grande")
#preparar_refrigerante("guaraná", "grande")

def fazer_combo_bigmac (nome, tamanho_batata, tipo, tamanho_bebida):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo, tamanho_bebida)

#fazer_combo_bigmac ("samuel", "grande", "guaraná", "grande")

def soma(num1,num2):
    resultaf = num1 + num2
    return resultaf   #resultado da função retornará assim, podendo ser usada fora da função
x = float(input("Digite o primeiro número: ")) 
y = float(input(f"Digite o segundo número: "))
resultado = soma(x,y)   
print(f"{resultado: .1f}")


